import pickle
import scipy
import numpy as np
import tensorflow as tf
import pandas as pd

model = tf.keras.models.load_model('./assets/model.keras')
with open("./assets/vectorizer.pickle", "rb") as f:
    vectorizer = pickle.load(f)

def classification(payload):
    message = ""
    query = vectorizer.transform([payload])
    
    transformed_query = scipy.sparse.csr_matrix.todense(query)
    
    prediction = model.predict(transformed_query)
    percentage = prediction[0][0]
    
    if percentage > 0.6:
        message = "ALERT! THIS MIGHT BE AN SQL INJECTION ATTACK ATTEMPT!"
    else:
        message = "SAFE! This is not an SQL injection attack attempt."
        
    return message, percentage * 100