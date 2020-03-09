import views
import db
from flask import Flask
    
def create_app():
    app = Flask(__name__)
    db.configure(app)
    views.configure(app)
    return app