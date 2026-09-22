from datetime import datetime, timezone
from flask import Flask, render_template
from flask_bootstrap import Bootstrap4

app = Flask(__name__)

bootstrap = Bootstrap4(app)


@app.route('/')
def index():
    return render_template('index.html', name='Kimberly',
                           current_time=datetime.now(timezone.utc).isoformat())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name,
                           current_time=datetime.now(timezone.utc).isoformat())
