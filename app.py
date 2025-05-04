import os
from flask import Flask, jsonify, request, abort
from garage import press_remote_garage, press_remote_gate
from dotenv import load_dotenv
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='/var/log/garage_access.log',
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
    logging.info("Garage door triggered")
    print("Garage door triggered, print.")
    press_remote_garage()
    return jsonify({'status': 'Garage door triggered'})


@app.route('/gate/open', methods=['POST'])
def open_gate():
    auth_header = request.headers.get('Authorization')
    if not auth_header or auth_header != f"Bearer {API_KEY}":
        abort(401)
    logging.info("Gate triggered")
    print("Gate triggered, print.")
    press_remote_gate()
    return jsonify({'status': 'Gate triggered'})
