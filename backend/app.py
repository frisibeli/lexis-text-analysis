from flask import Flask, request, jsonify
from sklearn.externals import joblib

HOST = "0.0.0.0"
PORT = 8080

app = Flask(__name__)


@app.route('/api/predict', methods=['GET', 'POST'])
def predict():
	input_text = "I hope this works"
	vectorizer = joblib.load('vectorizer.pkl')
	classifier = joblib.load('model.pkl')
	
	tokenized_input = vectorizer.transform([input_text])

	prediction_rbf = classifier.predict(tokenized_input)
	priediction_proba = classifier.predict_proba(tokenized_input)
	qwe = zip(classifier.classes_, priediction_proba[0]) #shows all propabilities
	asd = {k:v for k,v in qwe}
	asd['feeling'] = prediction_rbf[0]

	return jsonify({'response':asd})

if __name__ == "__main__":
	app.run(host=HOST, port=PORT, debug=True)
