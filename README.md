# physical-to-digital-workflow

## Purpose
To convert a hand-drawn design or workflow into digital form.

## Table of Contents
1. [Setup](#installation)
2. [Usage](#usage)

## Setup

1. Clone the repository:
    ```
    git clone https://github.com/RaghubirChimni/physical-to-digital-workflow.git
    ```
2. Navigate to the project directory:
    ```
    cd physical-to-digital-workflow
    ```
3. Activate Virtual Environment
    ``` 
    python -m venv venv
    source venv/bin/activate
    ```
4. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```
5. Obtain your [OpenAI API key](https://platform.openai.com/api-keys) & store it in .env

## Usage
1. Follow steps above

2. Take a picture of your hand-drawn workflow, ensure the words in each shape are  clearly-written. Must be in .png or .jpeg form.

3. Run the script
   ```
   python3 main.py <path to IMG>
   ```

4. Open workflow_diagram.png to see the digital version of your workflow.

5. Deactivate virtual environment when done.
    ``` 
    deactivate 
    ```