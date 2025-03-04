from flask import Flask
import os

app = Flask(__name__, 
            template_folder=os.path.abspath('templates'),
            static_folder=os.path.abspath('static'))

# Set a secure secret key
app.secret_key = '3b9f8a7c5d6e4f2a1b0c9d8e7f6a5b4c'

from app import routes