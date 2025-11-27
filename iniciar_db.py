import sqlite3

def crear_tabla():
    conexion = sqlite3.connect("base_datos_crypto.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS precios_bitcoin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            hora TEXT,
            precio_usd REAL
        )
    """)

    conexion.commit()
    conexion.close()
    print("✅ Base de datos y tabla creada con éxito.")

if __name__ == "__main__":
    crear_tabla()