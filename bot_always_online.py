from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hi viewer, I am currently online. Thanks for checking on me though!"

def run():
  app.run(host='0.0.0.0',port=8080)

def always_online():
    t = Thread(target=run)
    t.start()