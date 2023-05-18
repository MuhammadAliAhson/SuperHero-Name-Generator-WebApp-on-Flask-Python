from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('hero_names.h5')

# Load the tokenizer
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

char_to_index = tokenizer.word_index
index_to_char = dict((value, key) for key, value in char_to_index.items())

max_len = 33


def name_to_seq(name):
    return [tokenizer.texts_to_sequences(c)[0][0] for c in name]


def generate_name(seed):
    for i in range(40):
        seq = name_to_seq(seed)
        padded = tf.keras.utils.pad_sequences([seq], padding='pre', maxlen=max_len - 1, truncating='pre')
        pred = model.predict(padded)[0]
        pred_char = index_to_char[np.argmax(pred)]
        seed += pred_char

        if pred_char == '\t':
            break

    return seed


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['input_text']

    generated_name = generate_name(input_text)

    return render_template('index.html', input_text=input_text, results=generated_name)


if __name__ == '__main__':
    app.run(debug=True)
