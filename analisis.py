import requests

# Ruta de la API para analizar un archivo comprimido en formato bz2 y realizar el análisis de números de coincidencias.
# Recibe una solicitud POST con un archivo comprimido en formato bz2.
# Realiza el análisis de números de coincidencias en el archivo.
# Devuelve los resultados del análisis en formato JSON.

app = Flask(__name__)

@app.route('/')
def index():

#Ruta principal que renderiza la página index.html.

    return render_template('index.html')

@app.route('/analisis', methods=['POST'])
def analizar_archivo():
    
    try:
        archivo = request.files['archivo']
    except KeyError:
        return jsonify({'error': 'No se proporcionó ningún archivo en la solicitud POST.'}), 400

    datos = []
    with bz2.open(archivo, 'rt') as f:
        df = pd.read_csv(f, sep=',', header=None, names=["Time", "Duration", "SrcDevice", "DstDevice", "Protocol", "SrcProt", "DstPort", "SrcPackets", "DstPackets", "SrcBytes", "DstBytes"])
        datos = df.to_dict(orient='records')

    return jsonify(datos)

if __name__ == '__main__':
    app.run()
