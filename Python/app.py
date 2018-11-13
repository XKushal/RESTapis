from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return "hello from kushal"
  

  #pass

app.run(port=5000)