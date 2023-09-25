import mysql.connector
import os  # Agrega esta línea para importar el módulo os
from dotenv import load_dotenv

load_dotenv()

config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_DATABASE')
}

connection = mysql.connector.connect(**config)

cursor = connection.cursor()

def listarUsuarios():
    query = "SELECT * FROM usuarios"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

def insertarUsuario(nombre, correo):
    try: 
        query = "INSERT INTO usuarios (nombre, correo) values(%s, %s)"
        datos = (nombre, correo)

        cursor.execute(query, datos)
        connection.commit()
        print("Usuario insertado!")
    except mysql.connector.Error as error:
        print(f"Error al crear el usuario: {error}")
        connection.rollback()

def main():
    salir = False
    while(salir == False):
        print("Bienvenido al cliente de python para manejar una base de datos")
        print("\nOpciones:")
        print("1. Listar registros")
        print("2. Insertar registro")
        print("3. Actualizar registro")
        print("4. Eliminar registro")
        print("5. Limpiar consola")
        print("6. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1": 
            print("Listar usuarios:")
            listarUsuarios()
        if choice == "2":
            print("Se necesitan el nombre y correo del usuario: ")
            nombre = input("Por favor ingrese el nombre del usuario: ")
            correo = input("Por favor ingrese el correo del usuario: ")

            insertarUsuario(nombre, correo)
        if choice == "5":
            os.system('cls')
        if choice == "6":
            print("Hasta luego!")
            salir = True



if __name__ == "__main__":
    main()