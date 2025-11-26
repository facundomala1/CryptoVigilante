# CryptoVigilante 🚀
Sistema de integración y monitoreo de precios de Bitcoin.

## 📋 Descripción
Este proyecto implementa un ciclo ETL (Extract, Transform, Load) automatizado que consulta la API de CoinGecko y expone los datos a través de una API REST propia construida con FastAPI.

## 🛠 Tecnologías
- **Lenguaje:** Python 3.10+
- **ETL:** Requests, CSV
- **API:** FastAPI, Uvicorn
- **Entorno:** Virtualenv (venv)

## ⚙️ Instalación y Uso

1. Clonar el repositorio.
2. Crear entorno virtual: `python -m venv venv`
3. Instalar dependencias:
   ```bash
   pip install requests fastapi uvicorn