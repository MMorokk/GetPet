import os
from loaders import *
from dotenv import load_dotenv
# from markupsafe import escape
from markdown import markdown
from flask import (
    Flask,
    render_template,
    url_for,
    request,
)
from flask_minify import minify

# load_dotenv()
info = load_toml(os.path.join(os.path.dirname(__file__), 'info.toml'))

app = Flask(__name__)

# Automatically minify html, css and js to 
# speed up loading times and save bandwith
minify(app=app, html=True, js=True, cssless=True)

# # Make environment variables available to all templates
# @app.context_processor
# def inject_info():
#     return {
#         "website_title": os.getenv("WEBSITE_TITLE", "GetPet"),
#         "please_contact": os.getenv("PLEASE_CONTACT", False),
#         "contact_address": os.getenv("CONTACT_ADDRESS", "Chicago, US"),
#         "contact_phone": os.getenv("CONTACT_PHONE", "+380999123921"),
#         "contact_email": os.getenv("CONTACT_EMAIL", "mail@example.com"),
#     }

@app.route("/")
def index():
    return render_template("index.html", 
                           header = info["home"]["header"], 
                           text = markdown(info["home"]["text"], extensions=['nl2br']),
                           button = info["home"]["button"])

@app.route("/about")
def about():
    return render_template("about.html",
                           header = info["about"]["header"], 
                           text = markdown(info["about"]["text"], extensions=['nl2br']))

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return render_template("index.html")
    else:
        return render_template("contact.html", 
                            geolocation_latitude=os.getenv("GEOLOCATION_LATITUDE"), 
                            geolocation_longitude=os.getenv("GEOLOCATION_LONGITUDE"),
                            )

@app.route("/pets")
def pets():
    return render_template("pets.html")

if __name__ == "__main__":
    app.run()