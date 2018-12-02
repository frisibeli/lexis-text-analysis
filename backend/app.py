from flask import Flask, request, jsonify

HOST = "0.0.0.0"
PORT = 8080

app = Flask(__name__)


@app.route('/api/predict', methods=['GET', 'POST'])
def predict():
	return jsonify({'response':'OK'})

if __name__ == "__main__":
	app.run(host=HOST, port=PORT, debug=True)
