from flask import Flask, request
from flask_cors import CORS, cross_origin
import chat as helena

app = Flask(__name__)

@app.route('/chat',methods=['POST'])
@cross_origin()
def chat():
    return helena.chat(request.json['entrada'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=4000)