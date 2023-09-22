from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def gpt4(prompt):
	completion = openai.ChatCompletion.create(
		model="gpt-4",
    temperature=0.0,
		messages=[
      {"role": "system", "content": "You are a material science PHD student."},
      {"role": "user", "content": f"{prompt}"}
		]
	)

	return completion.choices[0].message.content
	
def gpt_35_turbo_16k(prompt):
	completion = openai.ChatCompletion.create(
		model="gpt-3.5-turbo-16k",
    temperature=0.0,
		messages=[
      {"role": "system", "content": "You are a material science PHD student."},
      {"role": "user", "content": f"{prompt}"}
		]
	)

	return completion.choices[0].message.content
