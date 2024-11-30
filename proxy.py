from flask import Flask
import httpx

app = Flask(__name__)

# code stub 
# TODO: replace code stub and implement proxy logic
@app.route("/")
def helloWorld():
    return "<p>Hello world</p>"

class handleRequest:
    pass

# TODO: implement reverse proxy 