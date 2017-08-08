import os
import logging
import socket

from config import Config
from logging.handlers import SysLogHandler

class LoggerWrapper():
  logger = None

class ContextFilter(logging.Filter):
  
  hostname = socket.gethostname()

  def filter(self, record):
    record.hostname = ContextFilter.hostname
    return True

def get_syslog_handler():
  logger_host = Config.LOGGER_HOST
  logger_port = Config.LOGGER_PORT
  if not logger_port:
    logging.basicConfig()
    return None
  syslog = SysLogHandler(address=(logger_host, int(logger_port)))
  formatter = logging.Formatter('%(asctime)s %(name)s %(hostname)s: %(message)s', datefmt='%b %d %H:%M:%S')
  syslog.setLevel(logging.INFO)
  syslog.setFormatter(formatter)
  return syslog

def get_logger():
  if LoggerWrapper.logger is None:
    LoggerWrapper.logger = logging.getLogger('flask-backend-boilerplate')
    LoggerWrapper.logger.setLevel(logging.INFO)
    f = ContextFilter()
    LoggerWrapper.logger.addFilter(f)
    syslog_handler = get_syslog_handler()
    if syslog_handler:
      LoggerWrapper.logger.addHandler(syslog_handler)
  return LoggerWrapper.logger