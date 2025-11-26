import requests
import time
import csv
import os
from datetime import datetime

URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
ARCHIVO_CSV = "historial_bitcoin.csv"
INTERVALO_SEGUNDOS = 60

def guardar_en_csv(fecha, precio):
    archivo_existe = os.path.isfile(ARCHIVO_CSV)
    
    with open(ARCHIVO_CSV, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        if not archivo_existe:
            writer.writerow(["Fecha", "Hora", "Precio (USD)"])
            
        writer.writerow([fecha, datetime.now().strftime("%H:%M:%S"), precio])

def iniciar_monitoreo():
    print(f"--- Iniciando Monitor. Guardando en {ARCHIVO_CSV} ---")
    print("Presiona Ctrl + C para detener.")
    
    while True:
        try:
            respuesta = requests.get(URL)
            
            if respuesta.status_code == 200:
                datos = respuesta.json()
                precio = datos['bitcoin']['usd']
                fecha_hoy = datetime.now().strftime("%Y-%m-%d")
                
                guardar_en_csv(fecha_hoy, precio)
                
                print(f"✅ Dato guardado: ${precio} USD")
            else:
                print(f"❌ Error API: {respuesta.status_code}")
                
        except Exception as e:
            print(f"⚠️ Error: {e}")
            
        time.sleep(INTERVALO_SEGUNDOS)

if __name__ == "__main__":
    iniciar_monitoreo()