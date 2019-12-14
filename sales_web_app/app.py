from flask import Flask, request, jsonify, url_for, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
import os, sys

import config_app as config_app
app = Flask(__name__, template_folder='templates')
app.config.from_object(config_app)

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)
from user_app import user


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
app.register_blueprint(user, url_prefix='/user')
def main():
    app.run(debug=True, port=8000, host='0.0.0.0')

if __name__ == '__main__':
    main()