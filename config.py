import os


class Config(object):
    PORT = os.getenv("PORT", "5001")
    GUNICORN_TOTAL_WORKERS = int(os.getenv("GUNICORN_TOTAL_WORKERS", "1"))
    LOGGER_HOST = os.getenv("LOGGER_HOST", "localhost")
    LOGGER_PORT = os.getenv("LOGGER_PORT", False)
    GUNICORN_SYSLOG_ADDRESS = os.getenv("GUNICORN_SYSLOG_ADDRESS", "localhost")
