#!/bin/bash

# flask settings
export FLASK_APP=/home/pi/AlarmClockServer/app.py
export FLASH_DEBUG=0

flask run --host=0.0.0.0 --port=5000
