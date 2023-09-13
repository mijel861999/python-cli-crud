# Proyecto de Python con MySQL y Variables de Entorno

Este proyecto de Python es un ejemplo de cómo trabajar con una base de datos MySQL y configurar las variables de entorno para una configuración segura y flexible. En este proyecto, creamos una tabla en una base de datos MySQL y utilizamos la biblioteca `python-dotenv` para cargar las variables de entorno desde un archivo `.env`.

## Configuración

Asegúrate de tener Python 3.x instalado en tu sistema. Luego, sigue estos pasos para configurar el proyecto:

1. Clona este repositorio a tu máquina local:

```bash
git clone https://github.com/tu-usuario/python-mysql-env.git
```

2. Accede al directorio del proyecto:

cd python-mysql-env

3. Instala dependencias

pip install mysql-connector-python python-dotenv

4. Configura tus variables de entorno

DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_DATABASE=nombre_de_tu_base_de_datos

5. Ejecuta

python main.py
