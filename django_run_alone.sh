#!/bin/sh
echo "SCRIPT ACTIVE"
IPCHECK=$(hostname -I | awk '{print $1}')
echo $IPCHECK 
port=":8000"
echo $port
ipport="$IPCHECK$port"
cd Django_feedback_app/

# python3 initdb.py 
python3 manage.py runserver $ipport

