# Primer Parcial
## Programación Web III - RESTful Singleton

### Antes de Empezar:

1. Realiza un **Fork** de este repositorio:

![Repositorio del Primer Parcial](https://live.staticflickr.com/65535/53639842480_6cd31a3bf6_z.jpg)

2. Si vas a trabajar en tu equipo local clona el nuevo repositorio resultado del **Fork** y ábrelo con **VSCode** o el editor de tu preferencia para trabajar tu solución. También puedes trabajar tu solución en **GitHub Codespaces**.

3. Completa tus datos personales en la siguiente tabla:
    | Nombre   | Apellido   | CI   |
    | -------- | ---------- | ---- |
    | PABEL DANTE | CHURATA APAZA | 9230639 |

4. Realiza un commit de esta modificación y sube los cambios a tu repositorio remoto ejecutando los siguientes comandos desde la terminal de tu equipo local o desde **GitHub Codespaces**:
    ```bash
    git add .
    git commit -m "datos actualizados"
    git push origin main
    ```
5. En la terminal ejecuta el siguiente comando para instalar las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

### Contexto:
Te han contratado como **Junior Back-End Developer** en una empresa de desarrollo de apps para dispositivos móviles. Tu primera tarea es desarrollar una **API RESTful** que permita administrar la información de las partidas de un juego de **Adivina el número** que se encuentra en desarrollo. Cada partida tiene la siguiente información:
- **id**: Identificador único de la partida.
- **player**: Nombre del jugador.
- **number**: Número a adivinar.
- **attempts**: Lista de intentos realizados por el jugador.
- **status**: Estado de la partida.

La lógica del juego es la siguiente: 
- El jugador crea una partida enviando su nombre.
- El servidor genera un número aleatorio entre 1 y 100.
- El jugador envía un número para adivinar.
- Si el número enviado por el jugador es igual al número generado por el servidor, la partida finaliza y se muestra un mensaje de felicitaciones.
- Si el número enviado por el jugador es menor al número generado por el servidor, se muestra un mensaje indicando que el número a adivinar es mayor.
- Si el número enviado por el jugador es mayor al número generado por el servidor,  se muestra un mensaje indicando que el número a adivinar es menor.

### Tareas:
Construye una **API RESTful** que permita realizar las operaciones **CRUD** sobre las partidas del juego de **Adivina el número**. La **API** debe permitir realizar las siguientes operaciones:
1. Crear una partida.
2. Listar todas las partidas.
3. Buscar una partida por su id.
4. Buscar una partida por el nombre del jugador.
5. Actualizar los intentos de una partida.
6. Eliminar una partida.

La **API RESTful** debe estar construida con el patrón de diseño **SINGLETON** y debe cumplir con los principios de desarrollo de Software **DRY, KISS, YAGNI y la S de SOLID**.

### Rutas y resultados esperados:
1. POST `/guess`
    - Datos a enviar:
    ```json
    {
        "player": "Julian"
    }
    ```
    - Respuesta Esperada:
    ```json
    {
        "player": "Julian",
        "number": 50,
        "attempts": [],
        "status": "En Progreso"
    }
    ```
2. GET `/guess`
   - Respuesta Esperada:
    ```json
    {
        "1":{
            "id": 1,
            "player": "Julian",
            "number": 50,
            "attempts": [],
            "status": "En Progreso"
        }
    }
    ```
3. GET `/guess/1`
   - Respuesta Esperada:
    ```json
    {
        "1":{
        "player": "Julian",
        "number": 50,
        "attempts": [],
        "status": "En Progreso"
    }
    }
    ```
4. GET `/guess/?player=Julian`
   - Respuesta Esperada:
    ```json
    {
        "1":{
            "player": "Julian",
            "number": 50,
            "attempts": [],
            "status": "En Progreso"
        }
    }
    ```
5. PUT `/guess/1`
    - Datos a enviar:
    ```json
    {
        "attempt": "25"
    }
    ```
    - Respuesta Esperada:
    ```json
    {
        "message": "El número a adivinar es mayor"
    }
    ```
6. GET `/guess`
   - Respuesta Esperada:
    ```json
    {
        "1":{
        "player": "Julian",
        "number": 50,
        "attempts": [25],
        "status": "En Progreso"
        }
    }
    ```
7. PUT `/guess/1`
    - Datos a enviar:
    ```json
    {
        "attempt": "75"
    }
    ```
    - Respuesta Esperada:
    ```json
    {
        "message": "El número a adivinar es menor"
    }
    ```
8. GET `/guess`
   - Respuesta Esperada:
    ```json
    {
        "1":{
        "player": "Julian",
        "number": 50,
        "attempts": [25, 75],
        "status": "En Progreso"
        }
    }
    ```
9. PUT `/guess/1`
    - Datos a enviar:
    ```json
    {
        "attempt": "50"
    }
    ```
    - Respuesta Esperada:
    ```json
    {
        "message": "¡Felicitaciones! Has adivinado el número"
    }
    ```
10. GET `/guess`
   - Respuesta Esperada:
    ```json
    {
        "1":{
        "player": "Julian",
        "number": 50,
        "attempts": [25, 75, 50],
        "status": "Finalizado"
        }
    }
    ```
11. DELETE `/guess/1`
    - Respuesta Esperada:
    ```json
    {
        "message": "Partida eliminada"
    }
    ```
12. GET `/guess`
    - Respuesta Esperada:
     ```json
     {}
     ```

### Entrega:
1. La lógica de la API debe estar en el archivo `server.py` que se encuentra dentro de la carpeta `solution`.
2. La lógica del cliente debe estar en el archivo `client.py` que se encuentra dentro de la carpeta `solution`.
3. Una vez tengas los puntos 1 y 2 completados, realiza un commit con el mensaje "Entrega Final" y sube los cambios a tu repositorio remoto ejecutando los siguientes comandos desde la terminal de tu equipo local o desde **GitHub Codespaces**:
    ```bash
    git add .
    git commit -m "Entrega Final"
    git push origin main
    ```
4. Una vez completado el paso anterior adjunta la **URL** de tu repositorio de **GitHub** en la tarea asignada en **Google Classroom**. 

### Restricciones:

Durante el examen solo puede consultar los siguientes recursos:
- [Patrón de Diseño Singleton](https://refactoring.guru/es/design-patterns/singleton)
- [Documentación Oficial de Python](https://docs.python.org/3/)
- [Documentación de HTTP Server](https://docs.python.org/3/library/http.server.html)
- [Documentación de la biblioteca requests](https://requests.readthedocs.io/en/latest/)
- [Documentación del modulo urllib.parse](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.parse_qs)

### IMPORTANTE: 
- **No** se permite el uso de frameworks como Flask, Django, FastAPI, etc.
- **No** se permite el uso de librerías externas que no estén dentro del archivo `requirements.txt`.
- **No** se permite el uso de bases de datos.
- **No** se permite el uso de archivos para almacenar la información.
- La **API** debe ser **RESTful**.
- La API debe cumplir con las operaciones **CRUD**.
- La **API** debe cumplir con las rutas y resultados esperados.
- La estructura de la **API** debe estar construida con el patrón de diseño **SINGLETON**.
- La **API** debe cumplir con los principios de desarrollo de Software **DRY, KISS, YAGNI y la S de SOLID**.
- Los ids de las partidas deben ser únicos y manejados de forma incremental correlativa.
