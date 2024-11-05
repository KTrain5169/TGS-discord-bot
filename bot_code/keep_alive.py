from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello, I am alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    """
    Starts the web server to keep the bot active.
    """
    t = Thread(target=run)
    t.start()
