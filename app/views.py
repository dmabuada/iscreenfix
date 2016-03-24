from app import app
from flask import render_template

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/isurance")
def isurance():
    return render_template('isurance.html')

@app.route("/it-services")
def it():
    return render_template('it-services.html')

@app.route("/computers")
def computers():
    return render_template('computers.html')

@app.route("/contact-us")
def contact():
    return render_template('contact-us.html')

if __name__ == "__main__":
    app.run()