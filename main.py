from flask import Flask, render_template, request
from replit import db

app = Flask('app', template_folder="templates", static_folder="static")

lst = []
db['text'] = "hi"

@app.route('/', methods = ['GET'])
def hello_world():
  text = request.args.get('text')
  print(text)
  db['text'] = str(db['text']) + " " + text
  return render_template('index.html', obj = db['text'])

@app.route('/display', methods = ['GET'])
def display():
  return render_template('index.html', obj = db['text'])

app.run(host='0.0.0.0', port=8080)