#!/bin/bash

set -e

mkdir -p /nanoserver/logs
touch /nanoserver/logs/celery.log

cd /nanoserver
tail -n 0 -f /nanoserver/logs/celery.log &

celery worker -A app.celery --concurrency=10 --loglevel=info
