# Home API

A simple Flask API for home automation (e.g., garage door), designed to be run as a service and proxied with Nginx.

## Features

Lightweight Flask API, WSGI entry point, garage control module, and a simple deployment script.

## Deployment with systemd

This project is intended to be run as a systemd service with Gunicorn.

### 1. Initial Setup

Clone, create a virtual environment, and install dependencies:

    git clone [https://github.com/vkotek/home-api.git](https://github.com/vkotek/home-api.git)
    cd home-api
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt


### 2. Create systemd Service

Create the service file:

    sudo nano /etc/systemd/system/home-api.service


Paste in the following, adjusting User, Group, and paths as needed:

    [Unit]
    Description=Gunicorn instance for pragensis.eu
    After=network.target
    
    [Service]
    User=www-data
    Group=www-data
    WorkingDirectory=/var/www/pragensis.eu
    ExecStart=/var/www/pragensis.eu/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:8001 --access-logfile - wsgi:app
    
    [Install]
    WantedBy=multi-user.target


Enable and start the service:

    sudo systemctl daemon-reload
    sudo systemctl start home-api
    sudo systemctl enable home-api


### 3. Deployment Script

The deploy.sh script automates pulling changes and restarting the service.

    #!/bin/bash
    cd /var/www/home-api
    git pull
    # /var/www/home-api/venv/bin/pip install -r requirements.txt
    sudo systemctl restart home-api


Make it executable:

    chmod +x deploy.sh


## API Endpoints

    POST /garage/open
    POST /gate/open

An Authorization header with API key must be passed with each request.

## Debugging
 
    journalctl -f -u pragensis.service # live logs
    systemctl restart pragensis.service
