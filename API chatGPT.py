import openai

# Set your OpenAI API key
openai.api_key = 'your api key'

# Define your prompt text
# Define your prompt text
prompt = "Write a poem about a robot who falls in love with the moon."

# Optional parameters for the API request
model_engine = "gpt-3.5-turbo-instruct"  # Recommended replacement for text-davinci-003
max_tokens = 150                   # Limit the response length (in tokens)
temperature = 0.7                   # Adjust the creativity (0=deterministic, 1=more random)

# Send the request and get the response
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=temperature
)

# Access the generated text
generated_text = response.choices[0].text

# Print the response
print(generated_text)


