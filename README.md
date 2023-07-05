## Lowfound openai web test project

### How to lauch this project:

1. Clone this repo and move to project main directory:
    - git clone git@github.com:Gudini108/lowfound-openai-test-project.git
    - cd lowfound_openai

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

5. Make migrations:
    - python3 manage.py migrate

for windows based system:
    - python manage.py migrate

6. Lauch project:
    - python3 manage.py runserver

for windows based system:
    - python manage.py runserver

Main page is available at http://127.0.0.1:8000/
