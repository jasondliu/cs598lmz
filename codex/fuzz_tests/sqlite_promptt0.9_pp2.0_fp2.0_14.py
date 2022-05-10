import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('../database/test.db')
if sqlite3 is None:
    print("Hay un problema con la conexion a la base de datos")
    exit()

"""
    Se crea la base de datos con los valores
"""
# Creamos la conexion y cursor
conn = sqlite3.connect("../database/test.db")
cursor = conn.cursor()

# Borramos la tabla
cursor.execute("DROP TABLE _usuarios")
cursor.execute("DROP TABLE _dispositivos")
cursor.execute("DROP TABLE _movimientos")

# Creamos la tabla usuarios
cursor.execute(
                """
                CREATE TABLE _usuarios(
                    cedula_usuario text,
                    usuario_email text,
                    usuario_nombre text,
                    usuario_apellido text,
                    usuario_clave text
                )
                """
            )

# Creamos la tabla dispositivos
cursor.execute
