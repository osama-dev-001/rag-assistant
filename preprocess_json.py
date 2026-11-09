import requests
import os
import json
import pandas as pd

def create_embedding(text_list):
    # https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })

    embedding = r.json()["embeddings"] 
    return embedding


jsons = os.listdir("resources/Tutorial_Jsons")
my_list = []
chunk_id = 0

for json_file in jsons:
    # print(json_file)
	with open(f"resources/Tutorial_Jsons/{json_file}") as f:
		content = json.load(f)
		# print(content)

	embeddings = create_embedding(c["text"] for c in content["chunks"])
	
	for i, chunk in enumerate(content["chunks"]):
		chunk["chunk_id"] = chunk_id
		chunk["embedding"] = embeddings[i]
		chunk_id += 1
		my_list.append(chunk)
  
df = pd.DataFrame.from_records(my_list)
print(df)
# a = create_embedding("hey buddy")
# print(a)