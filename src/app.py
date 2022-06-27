from flask import abort, json, jsonify, request, Flask, make_response
from datetime import datetime
import pandas as pd

app = Flask(__name__)

@app.route('/info',methods = ['GET'])
def info():
  res = {}
  res['msg'] = 'App works succesfully'
  res['gg'] = 'ggggggg'
  response = make_response(res)
  return response
