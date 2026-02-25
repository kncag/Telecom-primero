# 📉 Análisis de Evasión de Clientes (Churn) - Telecom X

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-150458?style=flat&logo=pandas)
![Seaborn](https://img.shields.io/badge/Seaborn-Data%20Viz-4cbfb4?style=flat)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter)

## 📌 Descripción del Proyecto
Este proyecto de Análisis de Datos tiene como objetivo identificar y comprender los factores principales que impulsan la cancelación de servicios (Churn) en **Telecom X**, una empresa ficticia de telecomunicaciones. A través de la extracción, limpieza y exploración profunda de los datos, buscamos extraer *insights* accionables que permitan a la compañía tomar decisiones estratégicas para retener a sus usuarios.

Este repositorio es parte del Challenge de Data Science.

## 🎯 Objetivos
- Cargar y estructurar datos anidados provenientes de una API en formato JSON.
- Realizar limpieza y transformación de datos (manejo de nulos, estandarización de categorías, codificación de variables).
- Aplicar Ingeniería de Características (*Feature Engineering*) para crear nuevas métricas como el `Gasto Diario` y el `Total de Servicios`.
- Ejecutar un Análisis Exploratorio de Datos (EDA) para encontrar correlaciones y patrones visuales del *Churn*.

## 🛠️ Tecnologías y Herramientas Utilizadas
- **Lenguaje:** Python
- **Manipulación de Datos:** Pandas, JSON, Requests
- **Visualización:** Matplotlib, Seaborn
- **Entorno:** Jupyter Notebook

## 📊 Principales Hallazgos (Insights)
Durante el análisis exploratorio, descubrimos patrones críticos sobre por qué los clientes abandonan la empresa:

1. **El Peligro del Corto Plazo:** Los clientes con contratos mensuales tienen una tasa de fuga del **42.7%**, mientras que los contratos a 2 años tienen una retención casi total (fuga del 2.8%).
2. **Fricción en Pagos:** El método de pago "Cheque Electrónico" concentra una fuga masiva del **45.3%**, lo que sugiere problemas en la plataforma de pagos o insatisfacción en ese segmento.
3. **Paradoja de la Fibra Óptica:** A pesar de ser un servicio premium, la Fibra Óptica presenta una evasión del **41.9%**, indicando posibles fallas en la calidad del servicio o problemas de precio/valor.
4. **Antigüedad Crítica:** Los primeros 10 meses son vitales. La mediana de antigüedad de los clientes que cancelan es de apenas 10 meses, en contraste con los 38 meses de los clientes retenidos.
5. **Efecto Ecosistema:** Los clientes que contratan 3 o más servicios adicionales (Seguridad, Respaldo, etc.) tienen mucha menor probabilidad de abandonar la empresa.

## 📂 Estructura del Repositorio
* `TelecomX_Data.json`: Dataset original crudo.
* `TelecomX_Cleaned.csv`: Dataset limpio y procesado listo para modelado predictivo.
* `TelecomX_LATAM.ipynb`: Jupyter Notebook que contiene todo el código fuente, dividido en:
  - `#📌 Extracción`
  - `#🔧 Transformación`
  - `#📊 Carga y análisis` (EDA)
  - `#🔗 Análisis de Correlación`
  - `#📄 Informe final`

## 🚀 Cómo ejecutar este proyecto
1. Clona este repositorio:
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)

2. Instala las dependencias necesarias:
---- pip install pandas matplotlib seaborn requests
3. Abre el archivo TelecomX_LATAM.ipynb en tu entorno de Jupyter Notebook o JupyterLab y ejecuta las celdas secuencialmente.

4. 
