import json
import re
from flask import Flask, request, url_for, redirect
import pyen

app = Flask(__name__, static_url_path='')

ECHO_NEST_API_KEY = "CYHEJAKXNKEGOCDXD"
en = pyen.Pyen(ECHO_NEST_API_KEY)

@app.route('/', methods=['GET'])
def index():
	return app.send_static_file('index.html')

@app.route('/search', methods=['GET'])
def search():
	'''
	return json.dumps({
		"genres": [
			{"name": "electro swing"},
		],
		"name": "Goldfish",
		"hotttnesss_rank": 3143,
		"images": [],
		"id": "AR813LR1187FB3F83A"
	})
	'''
	query = request.values.get('query')
	if not query:
		return json.dumps({

		})
	rx = re.compile('\W+')
	query = rx.sub(' ', query).strip()
	#artists = artist.search(name=query, buckets=['genre', 'hotttnesss_rank', 'images'])
	artists = en.get('artist/search', name=query, bucket=['genre', 'hotttnesss_rank', 'images'])
	if not artists:
		return json.dumps({"error": "fail bro"})
	print artists['artists']
	print artists['artists'][0]
	return json.dumps(artists['artists'][0])
	'''
	return json.dumps({
		'name': artists[0].name,
		'genres': artists[0].genres,
	})
	'''

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
