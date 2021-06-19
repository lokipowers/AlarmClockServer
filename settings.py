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