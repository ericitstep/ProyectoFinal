# Análisis de Datos con Flask y Pandas

Este proyecto utiliza Flask, Python y Pandas para realizar el análisis de números de coincidencias en archivos comprimidos en formato bz2. Proporciona una API que acepta archivos bz2 y devuelve los resultados del análisis en formato JSON.

## Instalación

1. Clona este repositorio en tu máquina local:
2. Navega al directorio del proyecto
3. Crea un entorno virtual e instala las dependencias

python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt


## Uso

1. Inicia la aplicación Flask:
2. Envía una solicitud POST a `http://localhost:5000/analisis` con un archivo bz2 para realizar el análisis de números de coincidencias.
3. Asegúrate de reemplazar `ruta/al/archivo.bz2` con la ruta al archivo bz2 que deseas analizar.
Obtendrás una respuesta en formato JSON con los resultados del análisis de números de coincidencias.




