#!/bin/bash

set -e

mkdir -p /nanoserver/logs
touch /nanoserver/logs/gunicorn.log
touch /nanoserver/logs/gunicorn-error.log
touch /nanoserver/logs/gunicorn-access.log

cd /nanoserver
tail -n 0 -f /nanoserver/logs/gunicorn*.log &

exec gunicorn app:app \
    --name task-handler \
    --bind 0.0.0.0:5000 \
    --timeout 120 \
    --workers 2 \
    --reload \
    --log-level=info \
    --log-file=/nanoserver/logs/gunicorn.log \
    --error-logfile=/nanoserver/logs/gunicorn-error.log \
    --access-logfile=/nanoserver/logs/gunicorn-access.log
