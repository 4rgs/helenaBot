import random
import json

import numpy as np
import tensorflow as tf


from nltk_utils import bag_of_words, tokenize
from data import all_words, tags

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)


model = tf.keras.models.load_model('my_model')


bot_name = "Helena"
print("¡Charlemos! ( tipea 'salir' para salir xD )")
while True:
    
    sentence = input("tu: ")
    if sentence == "salir":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = tf.convert_to_tensor(X)
    output = model(X)
    prob = output.numpy()
    pred = np.argmax(prob)

    
     
    tag = tags[pred]
    
    if prob[0][pred] > 0.60:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: Perdón no entiendo :( ...")
