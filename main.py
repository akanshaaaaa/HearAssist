from flask import Flask, render_template, request
from replit import db

def translate_text(target, text):
  import six
  from google.cloud import translate_v2 as translate

  translate_client = translate.Client()

  if isinstance(text, six.binary_type):
    text = text.decode("utf-8")
  result = translate_client.translate(text, target_language=target)
  return result["translatedText"]


app = Flask('app', template_folder="templates", static_folder="static")

lst = []
db['text'] = "hi"

translate_text("fr", "hello")

@app.route('/', methods = ['GET'])
def hello_world():
  text = request.args.get('text')
  print(text)
  db['text'] = str(db['text']) + " " + text
  return render_template('index.html', obj = db['text'])

@app.route('/display', methods = ['GET'])
def display():
  return render_template('index.html', obj = db['text'])

@app.route('/fr', methods = ['GET'])
def fr():
  return render_template('index.html', obj = translate_text("fr", db['text']))

app.run(host='0.0.0.0', port=8080)