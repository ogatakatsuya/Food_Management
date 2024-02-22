from flask import render_template
from app import app

from werkzeug.exceptions import NotFound

@app.route("/")
def hello():
    return render_template('hello.html')

@app.errorhandler(NotFound)
def show_404_page(error):
    msg = error.description
    print('Error:',msg)
    return render_template('errors/404.html', msg=msg)