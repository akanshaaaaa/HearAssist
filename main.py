from flask import Flask, render_template, request
from replit import db

app = Flask('app', template_folder="templates", static_folder="static")

lst = []

@app.route('/', methods = ['GET'])
def hello_world():
  text = request.args.get('text')
  print(text)
  return render_template('index.html')

app.run(host='0.0.0.0', port=8080)