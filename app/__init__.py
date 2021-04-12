from flask import Flask
from app.config import Config
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

UPLOAD_FOLDER = './app/static/uploads'

app.config.from_object(Config)

from app import views
