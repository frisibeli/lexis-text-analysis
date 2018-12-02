from flask import Flask, request, jsonify
from sklearn.externals import joblib
from flask_cors import CORS, cross_origin

HOST = "0.0.0.0"
PORT = 8080

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/predict', methods=['GET', 'POST'])
@cross_origin()
def predict():
	request_data = request.json
	input_text = request_data['input']
	vectorizer = joblib.load('vectorizer.pkl')
	classifier = joblib.load('model.pkl')
	
	tokenized_input = vectorizer.transform([input_text])

	prediction_rbf = classifier.predict(tokenized_input)
	priediction_proba = classifier.predict_proba(tokenized_input)
	probabilities = zip(classifier.classes_, priediction_proba[0]) #shows all propabilities
	response = {k:v for k,v in probabilities}
	response['feeling'] = prediction_rbf[0]

	return jsonify({'response':response})

if __name__ == "__main__":
	app.run(host=HOST, port=PORT, debug=True)
