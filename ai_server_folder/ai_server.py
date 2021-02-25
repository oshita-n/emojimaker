import fasttext
import MeCab
import pandas as pd
from flask import *
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def post():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    text = data["sentence"]
    result = model.predict(m.parse(text).strip("\n"))
    emoji = csv[1][int(result[0][0].strip("__label__"))]
    return {"result" : str(text + emoji)}
if __name__ == "__main__":
    model = fasttext.load_model("model_emoji.bin")
    m = MeCab.Tagger("-Owakati")
    csv = pd.read_csv("data.csv", header=None)
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True, ssl_context='adhoc')