import requests
import time
import sqlite3
from datetime import datetime

URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
DB_NAME = "base_datos_crypto.db"
INTERVALO_SEGUNDOS = 60

def guardar_en_db(fecha, precio):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    
    hora_actual = datetime.now().strftime("%H:%M:%S")
    cursor.execute("INSERT INTO precios_bitcoin (fecha, hora, precio_usd) VALUES (?, ?, ?)", 
            (fecha, hora_actual, precio))
    
    conexion.commit()
    conexion.close()

def iniciar_monitoreo():
    print(f"--- Iniciando Monitor SQL. Guardando en {DB_NAME} ---")
    
    while True:
        try:
            respuesta = requests.get(URL)
            if respuesta.status_code == 200:
                datos = respuesta.json()
                precio = datos['bitcoin']['usd']
                fecha_hoy = datetime.now().strftime("%Y-%m-%d")
                
                guardar_en_db(fecha_hoy, precio)
                print(f"✅ Dato guardado en DB: ${precio} USD")
            else:
                print(f"❌ Error API: {respuesta.status_code}")
        except Exception as e:
            print(f"⚠️ Error: {e}")
            
        time.sleep(INTERVALO_SEGUNDOS)

if __name__ == "__main__":
    iniciar_monitoreo()