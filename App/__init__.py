import os

from flask import Flask

import config
from .extentions import init_exts
from .urls import *


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_app():
    static_folder = os.path.join(BASE_DIR,'static')
    template_folder = os.path.join(BASE_DIR,'templates')

    app = Flask(__name__,
                static_folder=static_folder,
                template_folder=template_folder)
    app.config.from_object(config)

    init_exts(app=app)

    return app
