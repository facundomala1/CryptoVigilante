# CryptoVigilante 🚀
Sistema de integración y monitoreo de precios de Bitcoin.

## 📋 Descripción
Este proyecto implementa una arquitectura de microservicios para monitoreo financiero. 
1. **Worker ETL:** Un script en segundo plano consulta la API de CoinGecko y persiste los datos en una base de datos SQL.
2. **API REST:** Una interfaz construida con FastAPI que expone los datos almacenados para su consumo por clientes externos.

## 🛠 Tecnologías
- **Lenguaje:** Python 3.10+
- **Base de Datos:** SQLite (SQL)
- **API:** FastAPI, Uvicorn
- **Cliente HTTP:** Requests

## ⚙️ Instalación y Uso

1. Clonar el repositorio.
2. Crear entorno virtual: `python -m venv venv`
3. Instalar dependencias:
   ```bash
   pip install requests fastapi uvicorn