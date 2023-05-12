import os
import json
import requests

def read_json_files(directory):
    documents = []

    # Loop through all the files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a JSON file
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            with open(filepath) as file:
                # Load the JSON data from the file
                data = json.load(file)
                # Append each string in the JSON data to the documents list
                for document in data:
                    documents.append(document)

    return documents

# Replace 'your_api_key' with your actual API key
api_key = 'your_api_key'
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

#url = 'https://api.openai.com/v1/engines/davinci-codex/completions'

url = 'https://api.openai.com/v1/completions'

# Replace 'your_prompt' with your desired input prompt
#prompt = 'your_prompt'

def make_request(prompt):
	data = {
  "model": "text-davinci-003",
  "prompt": prompt,
  "max_tokens": 1000,
  "temperature": 0,
  #"top_p": 1,
  "n": 1,
  #"stream": False,
  #"logprobs": None,
  #"stop": "\n"
}


	response = requests.post(url, headers=headers, json=data)
	response_json = response.json()

	if response.status_code == 200:
	    generated_text = response_json['choices'] #[0]['text']
	    print(f"Generated text: {generated_text}")
	else:
	    print(f"Error: {response_json}")


def main():
	#documents = read_json_files('data/json')
	#doc = documents[4]
	#print(doc)
	#print("---------")
	#print(len(doc))
	make_request("Que crees que es importante saber para usar la API de chatGPT?")

if __name__ == "__main__":
    main()
