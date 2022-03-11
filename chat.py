import random
import json
from flask import  jsonify
import numpy as np
import tensorflow as tf


from nltk_utils import bag_of_words, tokenize
from data import all_words, tags

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)


model = tf.keras.models.load_model('helena')
entrada = ""
bot_name = "Helena"

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
    if prob[0][pred] > 0.60:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = (f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        response = (f"{bot_name}: Perdón no entiendo :( ...")
    print(response)
    return jsonify({"message":response})

