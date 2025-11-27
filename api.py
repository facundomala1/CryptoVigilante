from fastapi import FastAPI
import sqlite3

app = FastAPI()
DB_NAME = "base_datos_crypto.db"

# Función auxiliar para conectarnos a la DB
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row 
    return conn

@app.get("/")
def home():
    return {"mensaje": "API Crypto SQL Activa v2.0"}

@app.get("/historial")
def obtener_historial():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM precios_bitcoin")
    filas = cursor.fetchall()
    conn.close()
    return filas

@app.get("/ultimo")
def obtener_ultimo_precio():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM precios_bitcoin ORDER BY id DESC LIMIT 1")
    dato = cursor.fetchone()
    conn.close()
    
    if dato:
        return {
            "moneda": "Bitcoin",
            "precio": dato["precio_usd"],
            "fecha": dato["fecha"],
            "hora": dato["hora"]
        }
    else:
        return {"error": "No hay datos en la base de datos"}