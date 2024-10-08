from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  CORS(app)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  
  db.init_app(app)
  
  from . import routes
  app.register_blueprint(routes.bp)
  
  return app