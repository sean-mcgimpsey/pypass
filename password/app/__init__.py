from flask import Flask, request, g
import redis
from config import Config
from flask_bootstrap import Bootstrap
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

db = redis.StrictRedis(host="127.0.0.1", port=6379, decode_responses=True)

#db = SQLAlchemy(app)


from app import routes