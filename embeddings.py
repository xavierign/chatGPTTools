import openai
import pandas as pd
import numpy as np
import requests
from sklearn.metrics.pairwise import cosine_similarity

# Set up OpenAI API
openai.api_key = 'your_api_key'

# Load CSV file into DataFrame
#df = pd.read_csv('dataQ1.csv')

def get_embedding(text, model="text-embedding-ada-002"):
   text = str(text).replace("\n", " ")
   return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']

# remove comment to calculate embeddings
#df['ada_embedding'] = df['txt'].apply(get_embedding)
#df.to_csv('embedded_1k_reviews.csv', index=False)


# Load your CSV file into a DataFrame
#df = pd.read_csv('embedded_1k_reviews.csv')

# Function to convert string representation of a list to an actual list of floats
def str_to_list(embedding_str):
    return np.array([float(x) for x in embedding_str.strip('[]').split(',')])

# Transform the 'adaembedding' column to list format
#temp_list = df['ada_embedding'].apply(str_to_list)

# Get the embedding of another string
baseline1 = "Le diría a mi jefe que los requermientos nutricionales de los productos A y B (grasas, calcio, vitaminas y colesterol) no se pueden obtener mezclado los compuestos Y, V, W."
baseline2 = "Le recomendaria revisar los requerimientos máximos y mínimos, revisar los aportes de cada compuesto, o bien buscar otra materia prima para la mezcla"
baseline = baseline1 + " " + baseline2

baseline_emb = get_embedding(baseline)

# Calculate the cosine similarity between the other string's embedding and the embeddings in the DataFrame
#df['cosine_similarity'] = temp_list.apply(lambda x: cosine_similarity([x], [baseline_emb])[0][0])
#df.to_csv('embedded_1k_reviews_cos.csv', index=False)

#print(baseline_emb)
print(cosine_similarity([get_embedding("le diria que revise los datos")], [baseline_emb]))
