import json

from flask import Flask, render_template, request, redirect, url_for, jsonify
from modules.utils.logger import get_logger
from modules.handlers.error_handler import handle_error
from modules.helper import get_req_metadata

LOGGER = get_logger()


class HelloHandler(object):
    @staticmethod
    def hello(endpoint):
        try:
            LOGGER.info("hello hit")
            req_metadata = get_req_metadata()
            res_json = json.dumps(req_metadata)
            return res_json
        except Exception as exception:
            return handle_error(endpoint=endpoint, e=exception)
