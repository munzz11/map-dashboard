from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# API configuration
API_BASE_URL = os.getenv('API_URL', 'http://data-gateway:8080')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/deployments')
def get_deployments():
    try:
        response = requests.get(f'{API_BASE_URL}/deployments')
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/platforms/<deployment>')
def get_platforms(deployment):
    try:
        response = requests.get(f'{API_BASE_URL}/platforms/{deployment}')
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/locations')
def get_locations():
    deployment = request.args.get('deployment')
    platform = request.args.get('platform')
    
    try:
        params = {}
        if deployment:
            params['deployment'] = deployment
        if platform:
            params['platform'] = platform
            
        response = requests.get(f'{API_BASE_URL}/locations', params=params)
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/download_kml/<deployment>')
def download_kml(deployment):
    try:
        response = requests.get(f'{API_BASE_URL}/download_kml/{deployment}')
        return response.content, response.status_code, {
            'Content-Type': 'application/vnd.google-earth.kml+xml',
            'Content-Disposition': f'attachment; filename={deployment}_track.kml'
        }
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    host = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_RUN_PORT', '5001'))
    app.run(host=host, port=port, debug=True) 