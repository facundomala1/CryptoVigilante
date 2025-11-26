# Endpoint 3: Obtener solo el último precio registrado (Lógica de negocio)
@app.get("/ultimo")
def obtener_ultimo_precio():
    ultimo_dato = None
    try:
        with open(ARCHIVO_CSV, mode='r') as file:
            reader = csv.DictReader(file)
            # Recorremos todo para quedarnos con el final
            for row in reader:
                ultimo_dato = row
        
        if ultimo_dato:
            return {
                "moneda": "Bitcoin",
                "precio_actual": f"${ultimo_dato['Precio (USD)']}",
                "actualizado_a_las": ultimo_dato['Hora']
            }
        else:
            return {"mensaje": "No hay datos aún"}
            
    except FileNotFoundError:
        return {"error": "El sistema de monitoreo no está activo"}