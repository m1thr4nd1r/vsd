import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def vsd():
	if request.method == 'GET':
		return render_template('index.html')
	elif request.method == 'POST':
		source = request.form['source']
		value = request.form['value']
		days = request.form['days']
		
		cities = ['Salvador', 'Sao Paulo']
		hotels = ['Ibis', 'Pestana']

		return render_template('results.html',cities = cities, hotels = hotels);