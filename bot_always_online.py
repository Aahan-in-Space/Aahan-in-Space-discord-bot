from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hi viewer, I am currently online. Thanks for checking on me though! This only means that my server is online, there can sometimes be other errors meaning I am unable to be online in Discord."

def run():
  app.run(host='0.0.0.0',port=8080)

def always_online():
    t = Thread(target=run)
    t.start()