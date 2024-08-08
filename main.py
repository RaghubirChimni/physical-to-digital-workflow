import base64
import sys
import os
from dotenv import load_dotenv
import requests
import json
from graphviz import Digraph
  
# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  
def api_call(api_key, base64_image):
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }

  payload = {
    "model": "gpt-4o",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "You are supposed to identify different things of a workflow diagram (like a LucidChart). Tell me the flow of something including the words of each process & its shape. Tell me in this JSON form to show data & relationships { <name>: { shape: <shape>, color: <color>, children: [<children-names>] } } . No backticks or json prefix. Ensure the children are correct, especially for ending nodes. Return JSON format without any additional text or info. If no colors detected anywhere, leave value as blank unless specified."
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
  }

  ####### API CALL ############
  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
  content = response.json()['choices'][0]['message']['content']
  return content

### Create the Workflow Diagram
def create_graph(workflow):
  dot = Digraph()

  for key, value in workflow.items():
    dot.node(key, shape=value['shape'])
    for child in value['children']:
      color = value['color'] 
      dot.edge(key, child, style='filled', fillcolor=color)
  dot.render('workflow_diagram', format='png', view=True)

if __name__ == "__main__":
  load_dotenv()
  api_key = os.getenv('OPENAI_API_KEY')
  image_path = sys.argv[1]
  
  # encode image for gpt
  base64_image = encode_image(image_path)
  
  # api call & JSON conversion
  response = api_call(api_key, base64_image)
  workflow_json = json.loads(response)
  
  # create workflow diagram with this
  create_graph(workflow_json)
