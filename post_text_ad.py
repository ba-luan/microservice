from flask import Flask, jsonify, request
import json

app = Flask(__name__)

vocab = {
	"vocab": [
			"#ad",
			"#sponsored",
			"advertisement"
	]
}


@app.route("/ping")
def ping():
  return "pong!"

@app.route("/api/vocab")
def get_vocab():
  return vocab


@app.route("/api/vocab", methods=['POST'])
def add_vocab():
	new_vocab = json.loads(request.data)
	for i in new_vocab['vocab']:
		if i not in vocab['vocab']:
			vocab['vocab'].append(i)
	
	return vocab

@app.route("/api/prediction", methods=['POST'])
def predict():
	post_text = json.loads(request.data)
	post_text = post_text['post_text']
	post_text_words = post_text.split()
	for word in post_text_words:
		if word in vocab['vocab']:
			return {"prediction": "sponsored"}	
		else:
			return {"prediction": "non-sponsored"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)