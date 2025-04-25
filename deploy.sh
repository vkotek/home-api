#!/bin/bash
cd /var/www/pragensis.eu
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart pragensis
