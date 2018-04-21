from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def ballar():
    return render_template('ballar.html')
