import views
import contact
import db
from flask import Flask


def create_app():
    app = Flask(__name__)
    db.configure(app)
    views.configure(app)
    # configurar extensoes
    contact.configure(app)
    # configurar as variaveis
    app.config['SECRET_KEY'] = 'asudhasiudhasuidhasdhasygadas'
    return app
