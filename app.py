from flask import Flask, request
from flask_cors import CORS, cross_origin
import chat as helena

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/chat',methods=['POST'])
def chat():
    return helena.chat(request.json['entrada'])

if __name__ == '__main__':
    app.run(debug=True, port=4000)