import requests

def create_embedding(text):
	r = requests.post("http://localhost:11434/api/embeddings",
	json={
		"model": "bge-m3",
		"prompt": text
	})

	embedding = r.json()['embedding']
	return embedding
	# print(embedding)


a = create_embedding("hey buddy")
print(a)