import pandas as pd
import requests

# URL directa al contenido raw del archivo JSON
url = "https://raw.githubusercontent.com/ingridcristh/challenge2-data-science-LATAM/main/TelecomX_Data.json"

# 1. Cargar los datos desde la API
response = requests.get(url)

# 2. Verificar estatus y convertir a DataFrame
if response.status_code == 200:
    data = response.json()
    # Usamos json_normalize porque los datos tienen estructura anidada (customer, phone, etc.)
    df = pd.json_normalize(data)
    
    # Mostrar las primeras filas
    print("Datos cargados exitosamente:")
    print(df.head())
else:
    print(f"Error al cargar los datos: {response.status_code}")
