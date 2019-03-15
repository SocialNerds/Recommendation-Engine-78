from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Dense, Concatenate, Dropout
from sklearn.model_selection import train_test_split
import tensorflow as tf
import pandas as pd
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

dataset = pd.read_csv('data/ratings.csv')

train, test = train_test_split(dataset, test_size=0.00002)

features_num = 10
# Users embedding features.
user_input = Input(shape=[1])
user_embedding = Embedding(len(dataset.user_id.unique()) + 1, features_num)(user_input)
user_vector = Flatten()(user_embedding)

# Books embedding features.
book_input = Input(shape=[1])
book_embedding = Embedding(len(dataset.book_id.unique()) + 1, features_num)(book_input)
book_vector = Flatten()(book_embedding)

# Concatenate features.
concatenated = Concatenate()([book_vector, user_vector])

# Create model.
layer1 = Dense(128, activation='relu')(concatenated)
dropout1 = Dropout(0.1)(layer1)
layer2 = Dense(64, activation='relu')(dropout1)
dropout2 = Dropout(0.1)(layer2)
output = Dense(1)(dropout2)
model = Model([user_input, book_input], output)
model.compile('adam', 'mean_squared_error')

# Train.
model.fit([train.user_id, train.book_id],
                         train.rating, epochs=15, batch_size=256)

# Evaluate.
predictions = model.predict([test.user_id, test.book_id])
[print(predictions[i], test.rating.iloc[i]) for i in range(0, len(test))]
