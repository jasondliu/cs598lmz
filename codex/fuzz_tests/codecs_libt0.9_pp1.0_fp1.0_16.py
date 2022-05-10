import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

datasets = {}

# read all datasets in the datasets/ subfolder
for datasetFile in listdir("dataset/") :
	with open("dataset/" + datasetFile) as json_file:
		datasets[datasetFile[:-5]] = json.load(json_file)

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	return render_template('index.html')

@app.route("/api/table/<string:t>")
def route(t):
	if t in datasets:
		return jsonify(datasets[t])

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
