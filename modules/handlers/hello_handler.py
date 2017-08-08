import json

from flask import Flask, render_template, request, redirect, url_for, jsonify
from modules.utils.logger import get_logger
from modules.handlers.error_handler import handle_error

LOGGER = get_logger()

class HelloHandler (object):

  @staticmethod
  def hello (endpoint):
    try:
      message = {'text':'hello'}
      LOGGER.info('hello hit')
      res_json = json.dumps(message)
      return res_json
    except Exception as exception:
      return handle_error(endpoint=endpoint, e=exception)