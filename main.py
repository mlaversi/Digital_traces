from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import requests

app = Flask(__name__)
g_analytics_url = 'https://analytics.google.com/analytics/web/#/p344233666/reports/intelligenthome'

@app.route('/', methods=["GET"])
def index():
  return render_template('index.html')

@app.route('/logs/', methods=["GET"])
def show_logs():
  return render_template('logs.html')



@app.route('/cookie/', methods=["GET"])
def cookie(): 
  return requests.get(g_analytics_url).text 

