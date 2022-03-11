from flask import Flask, request
import chat as helena
app = Flask(__name__)

@app.route('/chat',methods=['POST'])
def chat():
    return helena.chat(request.json['entrada'])

if __name__ == '__main__':
    app.run(debug=True, port=4000)