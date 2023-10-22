#!/bin/sh
echo "SCRIPT ACTIVE"
# choose sleeptime from db response time
time="20"
echo "Sleeping $time seconds "
sleep $time
echo "Awake"
echo "Grep data ..."
IPCHECK=$(hostname -I | awk '{print $1}')
echo $IPCHECK 

port=":8000"
echo $port

ipport="$IPCHECK$port"
python3 initdb.py 
cd Django_feedback_app/


python3 manage.py runserver $ipport

