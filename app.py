import os
import pydevd_pycharm
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = 'Hello World from the cluster foooo!'
    

    r = requests.get(url='https://api.nal.usda.gov/fdc/v1/170184?api_key=JBK60wLCEeZwNMVYoiRKbWU4lUJaeJFhYTC557ze')
    json = r.json()
    msg += str(json)
    
    return msg

def attach():
  if os.environ.get('WERKZEUG_RUN_MAIN'):
    print('Connecting to debugger...')
    pydevd_pycharm.settrace('0.0.0.0', port=9000, stdoutToServer=True, stderrToServer=True)

if __name__ == '__main__':
  print('Starting hello-world server...')
  # comment out to use Pycharm's remote debugger
  # attach()

  app.run(host='0.0.0.0', port=8080)
