from flask import Flask, render_template
import httpx

app = Flask(__name__)

# code stub 
# TODO: replace code stub and implement proxy logic
@app.route("/")
def helloWorld():
    return render_template('index.html')

class handleRequest:
    pass

# TODO: implement reverse proxy 