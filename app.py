# APP

from os import urandom
from flask import Flask, render_template as rend, session, request, url_for
from requests import get

app = Flask(__name__)
app.secret_key = urandom(13)

with get('https://apis.is/petrol') as response:
	if response:
		print(' * API Succesfully loaded', response)
		data = response.json()['results']
	else:
		print(' * API error', response)
		exit()

stations = []
for station in data:
    if station['company'] not in stations:
        stations.append(station['company'])


# lat, lon = data[INT]['geo']['lat'], data[INT]['geo']['lon']

@app.route('/')
def index():
	return rend('index.html', stations=stations, data=data)

@app.route('/company/<name>')
def company(name):
	return rend('layout.html')

@app.route('/station/<int:id>')
def gas_station(id):
	with get('AIzaSyBfdyGWkuYa49GV3cBpNUrmu-LTkfeZKfA') as map:
		pass
	return rend('layout.html')


# error <<<<<<<<<<<
@app.errorhandler(400)
def error400(error):
	return rend('error.html', error_type=400, error=error)
@app.errorhandler(401)
def error401(error):
	return rend('error.html', error_type=401, error=error)
@app.errorhandler(403)
def error403(error):
	return rend('error.html', error_type=403, error=error)
@app.errorhandler(404)
def error404(error):
	return rend('error.html', error_type=404, error=error)
@app.errorhandler(500)
def error500(error):
	return rend('error.html', error_type=500, error=error)
@app.errorhandler(502)
def error502(error):
	return rend('error.html', error_type=502, error=error)
@app.errorhandler(503)
def error503(error):
	return rend('error.html', error_type=503, error=error)
@app.errorhandler(504)
def error504(error):
	return rend('error.html', error_type=504, error=error)
# error <<<<<<<<<<<

if __name__ == "__main__":
	app.run(debug=True)
