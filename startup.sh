#!/bin/bash

# Set exit on error
set -e

echo "Starting AI Powered Python Wrapper Service MVP..."

# Load environment variables
source .env

echo "Initializing database..."
python -m sqlalchemy.orm create -u "$DATABASE_URL"

echo "Starting backend service..."
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Wait for services to start
sleep 5

echo "Checking service status..."
if ps aux | grep -v grep | grep "uvicorn main:app" > /dev/null; then
  echo "Services started successfully!"
else
  echo "Error: Services failed to start."
  exit 1
fi

echo "AI Powered Python Wrapper Service MVP is running."