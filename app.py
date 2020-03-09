import views
import contact
from flask import Flask

def create_app():
    app = Flask(__name__)
    views.configure(app)
    #configurar extensoes
    contact.configure(app)
    #configurar as variaveis
    return app