import os

class Config(object):
  PORT = os.getenv('PORT', '5001')
  GUNICORN_TOTAL_WORKERS = int(os.getenv('GUNICORN_TOTAL_WORKERS', '1'))
  SYSLOG_ADDRESS = os.getenv('SYSLOG_ADDRESS', 'localhost')