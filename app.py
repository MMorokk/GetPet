import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Make environment variables available to all templates
@app.context_processor
def inject_env_vars():
    return {
        'website_title': os.getenv('WEBSITE_TITLE', 'GetPet'),
    }

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"