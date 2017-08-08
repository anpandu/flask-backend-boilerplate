import os

def workers():
  return int(os.getenv('GUNICORN_TOTAL_WORKERS', '1'))

worker_class = 'eventlet'
workers = workers()
bind = "0.0.0.0:" + os.getenv('PORT', '5001')
timeout = 10800
syslog_addr = os.getenv('GUNICORN_SYSLOG_ADDRESS', 'udp://')
syslog = True
loglevel = 'info'
accesslog = '-'