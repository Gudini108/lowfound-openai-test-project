## Lowfound openai web test project

### How to lauch this project:


you would need Python, preferably latest version.

1. Clone this repo and move to project main directory:
    - git clone git@github.com:Gudini108/lowfound-openai-test-project.git
    - cd lowfound-openai-test-project


2. Create and activate virtual enviroment:
    - python3 -m venv venv
    - source venv/bin/activate


for windows based system:
    - python -m venv venv
    - source/Scripts/activate

3. upgrade pip:
    - python3 -m pip install --upgrade pip


for windows based system:
    - python -m pip install --upgrade pip

4. Install requirements.txt
    - pip install -r requirements.txt


5. Go to `gpt_lowfound/views.py`


6. In line `openai.api_key = 'AI_API_KEY'` change `AI_API_KEY` to your openai API key


7. Make migrations and migrate:
    - python3 manage.py makemigrations
    - python3 manage.py migrate

for windows based system:
    - python manage.py makemigrations
    - python manage.py migrate


8. Lauch project:
    - python3 manage.py runserver

for windows based system:
    - python manage.py runserver


9. Go to main project page at http://127.0.0.1:8000/


10. Register as a new user and enter your question to the AI.


### To run this project again:

1. Move to project main directory:
     - cd lowfound-openai-test-project
  
2. Run server via this command:
     - python3 manage.py runserver

for windows based system:
    - python manage.py runserver

3. Access main page at http://127.0.0.1:8000/
