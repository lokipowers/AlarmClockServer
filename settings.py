from flask.json import jsonify
from db import *

from flask import Flask, request, jsonifys

app = Flask(__name__)

def saveSetting(key, value):
  cursor = db.cursor()
  sql = "UPDATE configs set value = '" + value + "' where config_key = '" + key + "'"
  cursor.execute(sql)
  db.commit()  

def setLEDStatus(value):
  saveSetting('led_enabled', value)


def setRumbleStatus(value):
  saveSetting('rumble_enailed', value)

def setSnoozeDuration(value):
  saveSetting('snooze_duration', value)

def setAlarmStatus(value):
  saveSetting('alarm_running', value)


# ALARM CONTROL
@app.route('/start-alarm')
def startAlarm():
  #LEDSTRIP.startShow()
  # updateAlarmConfig('alarm_running', 'True')
  setAlarmStatus('True')
  response = subprocess.check_output(['sudo', 'bash', 'runAlarm.sh'])
  #response = subprocess.check_output(['sudo', 'python', 'Rumble.py'])
  return jsonify(response)


@app.route('/stop-alarm')
def stopAlarm():
  #LEDSTRIP.stopShow()
  # updateAlarmConfig('alarm_running', 'False')
  setAlarmStatus('False')
  return jsonify(True)

# LED
@app.route('/enable-led')
def enableLED():
  setLEDStatus('True')

@app.route('/disabled-lef')
def disableLED():
  setLEDStatus('False')

# Rumble
@app.route('/enable-rumble')
def enableRumble():
  setRumbleStatus('True')

@app.route('/disabled-rumble')
def disableRumble():
  setRumbleStatus('False')

# Snooze
@app.route('/set-snooze-duration', methods=['GET'])
def saveSnoozeDuration():
  setSnoozeDuration(request.args.get('snooze_duration'))


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
  return jsonify(cursor.fetchAll())