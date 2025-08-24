from flask import Flask, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    """Ruta principal que retorna saludo"""
    return jsonify({
        'message': 'Hola Mundo desde Python DevOps!',
        'version': '1.0.0',
        'timestamp': datetime.now().isoformat(),
        'framework': 'Flask'
    })

@app.route('/health')
def health_check():
    """Ruta de salud para verificar que la app funciona"""
    return jsonify({
        'status': 'OK', 
        'message': 'Aplicación funcionando correctamente'
    }), 200

@app.route('/info')
def info():
    """Información adicional de la aplicación"""
    return jsonify({
        'app_name': 'Python DevOps Practice',
        'python_version': os.sys.version,
        'flask_version': Flask.__version__
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)