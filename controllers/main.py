from flask import *
from extensions import mysql

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def main_route():
    options = {
        "session": False,
    }
    return render_template("index.html", options=options)