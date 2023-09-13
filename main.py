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

def main():
    print("Bienvenido al cliente de python para manejar una base de datos")
    print("\nOpciones:")
    print("1. Listar registros")
    print("2. Insertar registro")
    print("3. Actualizar registro")
    print("4. Eliminar registro")
    print("5. Salir")

    choice = input("Seleccione una opción: ")

    if choice == "1": 
        print("Listar usuarios:")
        listarUsuarios()


if __name__ == "__main__":
    main()