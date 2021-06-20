from db import *

def updateAlarm(id, args):
  cursor = db.cursor()
  sql = "UPDATE alarms set time = '" + args.time + "', date = '" + args.date + "', repeat_days = '" + args.repeat_days + "', enabled = 1 where ID = " + id
  cursor.execute(sql)
  db.commit()  

def createAlarm(args):
  cursor = db.cursor()
  sql = "INSERT INTO alarms (time, date, repeat_days, enabled) VALUES ('" + args.time + "', '" + args.date + "', '" + args.repeat_days + "', 1)"
  cursor.execute(sql)
  db.commit()

def setAlarmStatus(id, status):
  cursor = db.cursor()
  sql = "UPDATE alarms set enabled = " + status + " WHERE ID = " + id
  cursor.execute(sql)

def deleteAlarm(id):
  cursor = db.cursor()
  sql = "UPDATE alarms set deleted_at = NOW() WHERE ID = " + id
  cursor.execute(sql)

def getAlarms():
  cursor = db.cursor()
  sql = "SELECT time, date, repeat_days, enabled FROM alarms WHERE deleted_at IS NULL"
  cursor.execute(sql)
  return cursor.fetchall()

def getAlarm(id):
  cursor = db.cursor()
  sql = "SELECT time, date, repeat_days, enabled FROM alarms WHERE id = " + id
  cursor.execute(sql)
  return cursor.fetchall()