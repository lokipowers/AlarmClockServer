from flask import Flask, jsonify, request, send_file
from flask_cors import CORS

from led import Led

import subprocess
import time
#import configparser
#import mysql.connector
from db import *
from settings import *
from alarms import *

LEDSTRIP = Led()

#Config = configparser.ConfigParser()

# config
DEBUG = True

# Init app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
  return jsonify('pong!')





# SCREEN POWER
@app.route('/screen-power', methods=['GET'])
def screen_power():
  status = request.args.get('power')
  subprocess.check_output('sudo bash -c "echo ' + status + ' > /sys/class/backlight/rpi_backlight/bl_power"', shell=True)
  return jsonify(status)



#@app.route('/reboot', methods=['GET'])
#def reboot():
#  subprocess.check_output("reboot", shell=True)


# ALARM CONTROL
@app.route('/start-alarm')
def startAlarm():
  #LEDSTRIP.startShow()
  # updateAlarmConfig('alarm_running', 'True')
  saveSetting('alarm_running', 'True')
  response = subprocess.check_output(['sudo', 'bash', 'runAlarm.sh'])
  #response = subprocess.check_output(['sudo', 'python', 'Rumble.py'])
  return jsonify(response)


@app.route('/stop-alarm')
def stopAlarm():
  #LEDSTRIP.stopShow()
  # updateAlarmConfig('alarm_running', 'False')
  saveSetting('alarm_running', 'False')
  return jsonify(True)

# LED
@app.route('/enable-led')
def enableLED():
  setLEDStatus('True')
  return jsonify(True)

@app.route('/disable-led')
def disableLED():
  setLEDStatus('False')
  return jsonify(True)

# Rumble
@app.route('/enable-rumble')
def enableRumble():
  setRumbleStatus('True')
  return jsonify(True)

@app.route('/disabled-rumble')
def disableRumble():
  setRumbleStatus('False')
  return jsonify(True)

# Snooze
@app.route('/set-snooze-duration', methods=['GET'])
def saveSnoozeDuration():
  setSnoozeDuration(request.args.get('snooze_duration'))
  return jsonify(True)


# SCREEN BRIGHTNESS
@app.route('/set-screen-brightness', methods=['GET'])
def change_brightness():
  # Change screen brightness
  brightness = request.args.get('brightness')
  subprocess.check_output('sudo bash -c "echo ' + brightness + ' > /sys/class/backlight/rpi_backlight/brightness"', shell=True)
  return jsonify(request.args.get('brightness'))

 
@app.route('/get-screen-brightness', methods=['GET'])
def get_brightness():
  with open('/sys/class/backlight/rpi_backlight/brightness', 'r') as b:
    brightness = b.read()
  return brightness


# All Settings
@app.route('/get-settings')
def getSettings():
  cursor = db.cursor()
  sql = "SELECT * FROM configs"
  cursor.execute(sql)
  return jsonify(cursor.fetchall())


@app.route('/get-alarms')
def fetchAlarms():
  return jsonify(getAlarms())

@app.route('/create-alarm', methods=['GET'])
def makeAlarm():
  createAlarm(request.args.get('alarm'))
  return jsonify(getAlarms())

@app.route('/update-alarm/<id>', methods=['GET'])
def saveAlarm(id):
  updateAlarm(id, request.args.get('alarm'))

@app.route('/set-alarm-status/<id>', methods=['GET'])
def changeAlarmStatus(id):
  setAlarmStatus(id, request.args.get('status'))

@app.route('/delete-alarm/<id>', methods=['GET'])
def removeAlarm(id):
  deleteAlarm(id)

if __name__ == '__main__':
  app.run()
