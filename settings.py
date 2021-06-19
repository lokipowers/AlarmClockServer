from db import *

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


