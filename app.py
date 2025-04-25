import os
from flask import Flask, jsonify, request, abort
from garage import press_remote
from dotenv import load_dotenv
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='/var/log/garage_access.log'm
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

load_dotenv() # load env variables
app = Flask(__name__)

API_KEY = os.getenv('GARAGE_API_KEY')

@app.route('/')
def index():
    return "<h1>Welcome to pragensis.eu powered by Flask!</h1>"

@app.route('/garage/open', methods=['POST'])
def open_garage():
    auth_header = request.headers.get('Authorization')
    if not auth_header or auth_header != f"Bearer {API_KEY}":
        abort(401)

    press_remote()
    return jsonify({'status': 'Garage door triggered'})
