# RPG Docker API

Proyecto académico que implementa una API de un videojuego RPG sencillo utilizando contenedores Docker.

El objetivo del proyecto es demostrar el uso de tecnologías modernas de desarrollo backend como Docker, Docker Compose, FastAPI y PostgreSQL para crear una arquitectura modular basada en servicios.

---

# Tecnologías utilizadas

Este proyecto utiliza las siguientes tecnologías:

- Docker
- Docker Compose
- Python
- FastAPI
- PostgreSQL
- Git
- GitHub

Estas herramientas permiten crear una aplicación backend moderna ejecutada mediante contenedores.

---

# Descripción del proyecto

El sistema implementa una API REST que simula un sistema básico de combate RPG entre jugadores y enemigos.

Los jugadores tienen:

- nombre
- tipo elemental
- nivel

Los enemigos también tienen:

- nombre
- tipo elemental
- nivel

El sistema permite crear personajes, crear enemigos y simular combates entre ellos.

El combate se calcula teniendo en cuenta el nivel del personaje y las ventajas entre tipos elementales.

El nivel máximo que puede alcanzar un jugador es **nivel 5**.

---

# Tipos elementales

El juego incluye los siguientes tipos:

- Agua
- Fuego
- Planta
- Eléctrico
- Tierra
- Volador

Cada tipo tiene ventajas sobre otros tipos que influyen en el resultado del combate.

---

# Arquitectura del proyecto

El sistema utiliza una arquitectura basada en contenedores gestionados con Docker Compose.

Se utilizan dos servicios principales:

Backend
- API desarrollada en FastAPI
- Gestiona la lógica del juego

Base de datos
- PostgreSQL
- Almacena jugadores y enemigos

Ambos contenedores se comunican mediante una red interna de Docker.

También se utiliza un volumen persistente para almacenar los datos de la base de datos.

---

# Ejecución del proyecto

Para ejecutar el proyecto se debe ejecutar el siguiente comando dentro de la carpeta del proyecto:
# RPG Docker API

Proyecto académico que implementa una API de un videojuego RPG sencillo utilizando contenedores Docker.

El objetivo del proyecto es demostrar el uso de tecnologías modernas de desarrollo backend como Docker, Docker Compose, FastAPI y PostgreSQL para crear una arquitectura modular basada en servicios.

---

# Tecnologías utilizadas

Este proyecto utiliza las siguientes tecnologías:

- Docker
- Docker Compose
- Python
- FastAPI
- PostgreSQL
- Git
- GitHub

Estas herramientas permiten crear una aplicación backend moderna ejecutada mediante contenedores.

---

# Descripción del proyecto

El sistema implementa una API REST que simula un sistema básico de combate RPG entre jugadores y enemigos.

Los jugadores tienen:

- nombre
- tipo elemental
- nivel

Los enemigos también tienen:

- nombre
- tipo elemental
- nivel

El sistema permite crear personajes, crear enemigos y simular combates entre ellos.

El combate se calcula teniendo en cuenta el nivel del personaje y las ventajas entre tipos elementales.

El nivel máximo que puede alcanzar un jugador es **nivel 5**.

---

# Tipos elementales

El juego incluye los siguientes tipos:

- Agua
- Fuego
- Planta
- Eléctrico
- Tierra
- Volador

Cada tipo tiene ventajas sobre otros tipos que influyen en el resultado del combate.

---

# Arquitectura del proyecto

El sistema utiliza una arquitectura basada en contenedores gestionados con Docker Compose.

Se utilizan dos servicios principales:

Backend
- API desarrollada en FastAPI
- Gestiona la lógica del juego

Base de datos
- PostgreSQL
- Almacena jugadores y enemigos

Ambos contenedores se comunican mediante una red interna de Docker.

También se utiliza un volumen persistente para almacenar los datos de la base de datos.

---

# Ejecución del proyecto

Para ejecutar el proyecto se debe ejecutar el siguiente comando dentro de la carpeta del proyecto:
docker compose up

Este comando iniciará automáticamente todos los contenedores necesarios para ejecutar el sistema.

---

# Acceso a la API

Una vez iniciado el proyecto, la API estará disponible en:

http://localhost:8000

La documentación interactiva de la API se encuentra en:

http://localhost:8000/docs

Desde esta interfaz se pueden ejecutar todas las funciones del juego.

---

# Funcionalidades disponibles

La API permite:

- crear jugadores
- crear enemigos
- ejecutar combates
- subir de nivel hasta nivel máximo 5

---

# Posibles mejoras futuras

El proyecto podría ampliarse con:

- sistema de puntos de vida
- daño aleatorio en combate
- interfaz gráfica web
- sistema de ranking de jugadores
- inteligencia artificial para enemigos
