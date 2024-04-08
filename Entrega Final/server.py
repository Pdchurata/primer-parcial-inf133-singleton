from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import random

class GuessNumberGame:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.games = {}
        return cls._instance

    def create_game(self, player):
        game_id = len(self.games) + 1
        number_to_guess = 50
        game_data = {
            "player": player,
            "number": number_to_guess,
            "attempts": [],
            "status": "En Progreso"
        }
        self.games[game_id] = game_data
        return game_data

    def get_game_by_id(self, game_id):
        return self.games.get(game_id)

    def get_game_by_player(self, player):
        for game_id, game_data in self.games.items():
            if game_data["player"] == player:
                return game_data
        return None

    def update_attempts(self, game_id, attempt):
        game_data = self.games.get(game_id)
        if game_data:
            game_data["attempts"].append(attempt)
            if attempt == game_data["number"]:
                game_data["status"] = "Finalizado"
                return "felicitaciones ha adivinado el numero"
            elif attempt < game_data["number"]:
                return "El numero a adivinar es mayor"
            else:
                return "El numero a adivinar es menor"
        return None

    def delete_game(self, game_id):
        if game_id in self.games:
            del self.games[game_id]
            return "Partida eliminada"
        return None

class RESTRequestHandler(BaseHTTPRequestHandler):
    game_instance = GuessNumberGame()

    def do_GET(self):
        if self.path == "/guess":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(self.game_instance.games).encode("utf-8"))
        elif self.path.startswith("/guess/"):
            game_id = int(self.path.split("/")[-1])
            game_data = self.game_instance.get_game_by_id(game_id)
            if game_data:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({game_id: game_data}).encode("utf-8"))
            else:
                self.send_response(404)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"Error": "Partida no encontrada"}).encode("utf-8"))
        elif self.path.startswith("/guess/?player="):
            player = self.path.split("=")[-1]
            game_data = self.game_instance.get_game_by_player(player)
            if game_data:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({1: game_data}).encode("utf-8"))
            else:
                self.send_response(404)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"Error": f"No se encontró partida para el jugador {player}"}).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

    def do_POST(self):
        if self.path == "/guess":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            player = json.loads(post_data.decode("utf-8"))["player"]
            game_data = self.game_instance.create_game(player)
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(game_data).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

    def do_PUT(self):
        if self.path.startswith("/guess/"):
            game_id = int(self.path.split("/")[-1])
            content_length = int(self.headers["Content-Length"])
            put_data = self.rfile.read(content_length)
            attempt = int(json.loads(put_data.decode("utf-8"))["attempt"])
            message = self.game_instance.update_attempts(game_id, attempt)
            if message:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"message": message}).encode("utf-8"))
            else:
                self.send_response(404)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"Error": "Partida no encontrada"}).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

    def do_DELETE(self):
        if self.path.startswith("/guess/"):
            game_id = int(self.path.split("/")[-1])
            message = self.game_instance.delete_game(game_id)
            if message:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"message": message}).encode("utf-8"))
            else:
                self.send_response(404)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"Error": "Partida no encontrada"}).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()

if __name__ == "__main__":
    run_server()
