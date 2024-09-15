# API REST con Django Rest framework con autenticacion de usuario con JWT

## Objetivo
Crear una API REST con Django Rest Framework que haga autenticación de usuario con JWT y que implemente documentación interactiva con Swagger. La API debe permitir:
- Login
- Register
- Logout
- CRUD de tareas

Las tareas son del usuario que se ha logueado. Si no está logueado, no podrá realizar ninguna operación del CRUD.



## Endpoints de la API:

### Registro de Usuario

- `POST /api/register/  ` - Registrarse
  - **Request**: 
    ```json
    {
        "username": "usuario",
        "email": "usuario@example.com",
        "password": "contraseña_segura"
    }
    ```
  - **Response**:
    ```json
    {
        "username": "nuevo_usuario",
        "email": "usuario@example.com", 
    }
    ```
  - **Descripción**: Devuelve el `username`y `email` 

  ### Autenticación
- `POST /api/login/` - Iniciar sesión
  - **Request**: 
    ```json
    {
        "username": "usuario",
        "password": "contraseña_segura"
    }
    ```
  - **Response**:
    ```json
    {
     "refresh": "eyJhbGciOiJIUzI1NiIsIn...",
     "access": "eyJhbGciOiJIUzI1NiIsIn..."
    }
    ```
  - **Descripción**: Devuelve un `refresh token` y un `access token`.
    
##Instalación de la API REST

### Requisitos
- asgiref==3.8.1
- dj-rest-auth==6.0.0
- Django==5.1.1
- django-bootstrap3==24.2
- djangorestframework==3.15.2
- djangorestframework-simplejwt==5.3.1
- drf-yasg==1.21.7
- inflection==0.5.1
- packaging==24.1
- PyJWT==2.9.0
- pytz==2024.2
- PyYAML==6.0.2
- setuptools==74.1.2
- sqlparse==0.5.1
- tzdata==2024.1
- uritemplate==4.1.1

### Instalación:
1. Clonar el repositorio de GitHub con el comando:

    ```bash
    https://github.com/jrxjb/API.git
    ```

2. Entrar a la carpeta del proyecto:
    ```bash
cd \myapi
    ```
    
3. Crea y activa un entorno virtual:
    ```bash
    python -m venv env
    Usa `env\Scripts\activate`
    ```
4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
  
5. Configura las variables de entorno:
    - Crea un archivo `.env` en la raíz del proyecto y define las variables necesarias.
    ```env
    SECRET_KEY=tu_clave_secreta
    DEBUG=True
    DATABASE_URL=postgres://usuario:contraseña@localhost:5432/tu_base_de_datos
    ```

6. Realiza las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```

7. Crea un superusuario para acceder al panel de administración de Django:
    ```bash
    python manage.py createsuperuser
    ```

8. Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

