import random
import json
from flask import  jsonify
import numpy as np
import tensorflow as tf
import pyttsx3

from nltk_utils import bag_of_words, tokenize
from data import all_words, tags

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

model = tf.keras.models.load_model('helena')
print(model)
entrada = ""
bot_name = "Helena"

def onStart(name):
   print('starting', name)
def onWord(name, location, length):
   print('word', name, location, length)
def onEnd(name, completed):
   print('finishing', name, completed)

def chat(entrada):
    sentence = tokenize(entrada)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = tf.convert_to_tensor(X)
    output = model(X)
    prob = output.numpy()
    pred = np.argmax(prob)
    tag = tags[pred]
    response = ""
    engine = pyttsx3.init()
    engine.connect('started-utterance', onStart)
    engine.connect('started-word', onWord)
    engine.connect('finished-utterance', onEnd)
    print(prob[0][pred])
    if prob[0][pred] > 0.63:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = (f"{random.choice(intent['responses'])}")
    else:
        response = (f"Perdón no entiendo :( ...")
    print(response)
    engine.say(response)
    engine.startLoop()
    return jsonify({"nombre": bot_name,"mensaje":response})

