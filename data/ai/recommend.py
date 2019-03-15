from tensorflow.keras.models import load_model, Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Dot, Dense, Concatenate
from sklearn.model_selection import train_test_split
import tensorflow as tf
import numpy as np
import pandas as pd
import os

dataset = pd.read_csv('data/ratings.csv')
# print(dataset.head())

train, test = train_test_split(dataset, test_size=0.1, random_state=42)

users_num = len(dataset.user_id.unique())
books_num = len(dataset.book_id.unique())

# Users embedding features.
user_input = Input(shape=[1])
user_embedding = Embedding(users_num + 1, 5)(user_input)
user_vector = Flatten()(user_embedding)

# Books embedding features.
book_input = Input(shape=[1])
book_embedding = Embedding(books_num + 1, 5)(book_input)
book_vector = Flatten()(book_embedding)

# Concatenate features.
concatenated = Concatenate()([book_vector, user_vector])

# Create model.
layer1 = Dense(64, activation='relu')(concatenated)
layer2 = Dense(32, activation='relu')(layer1)
output = Dense(1)(layer2)
model = Model([user_input, book_input], output)
model.compile('adam', 'mean_squared_error')

# Train.
model.fit([train.user_id, train.book_id],
                         train.rating, epochs=5, batch_size=32)

# Evaluate.
predictions = model.predict([test.user_id.head(10), test.book_id.head(10)])
[print(predictions[i], test.rating.iloc[i]) for i in range(0, 10)]
