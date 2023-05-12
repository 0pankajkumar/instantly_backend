from flask import Flask
from emails import email_blueprint

app = Flask(__name__)
app.secret_key = 'something simple for now'
app.register_blueprint(email_blueprint)