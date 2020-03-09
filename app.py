import views
import contact
import db
import admin
from flask import Flask


def create_app():
    app = Flask(__name__)
    db.configure(app)
    views.configure(app)
    # configurar extensoes
    contact.configure(app)
    admin.configure(app)
    # configurar as variaveis
    app.config['SECRET_KEY'] = 'asudhasiudhasuidhasdhasygadas'
    return app
