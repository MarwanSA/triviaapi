# Full Stack API Final Project

## Full Stack Trivia

Trivia API is created to play the game Trivia. 

##Installing Dependencies

Python 3.7

Follow instructions to install the latest version of python for your platform in the python docs

Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the /backend directory and running:

pip install -r requirements.txt
This will install all of the required packages we selected within the requirements.txt file.

Key Dependencies

Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.

SQLAlchemy is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

Flask-CORS is the extension we'll use to handle cross origin requests from our frontend server.

Database Setup

With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

psql trivia < trivia.psql
Running the server

From within the backend directory first ensure you are working using your created virtual environment.

To run the server, execute:

export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
Setting the FLASK_ENV variable to development will detect file changes and restart the server automatically.

Setting the FLASK_APP variable to flaskr directs flask to use the flaskr directory and the __init__.py file to find the application.



The `./backend` directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in app.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup. 

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. 


## API Endpoints: 

* GET /categories

Returns all the categories
URI:- http://127.0.0.1:5000/categories
Response
{
"categories": {
"1": "history",
"2": "science",
"3" : "Geography",
"4" : "History",
"5" : "Entertainment",
"6" : "Sports"
},
"success": true
}

* GET /questions

Returns all the questions 
URI:- http://127.0.0.1:5000/questions
Response
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "questions": [
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
        },
        {
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        },
        {
            "answer": "One",
            "category": 2,
            "difficulty": 4,
            "id": 18,
            "question": "How many paintings did Van Gogh sell in his lifetime?"
        }
    ],
    "success": true,
    "total_questions": 15
}



* DELETE /questions/<int:question_id>

Deletes question with given ID.
URI:- http://127.0.0.1:5000/questions/12
Response
{
  "id": 12,
  "message": "Question deleted successfully ",
  "success": true
}


* POST /questions

Inserting a new question.
URI:- http://127.0.0.1:5000/questions
JSON file format
{
"answer": "blue",
"category": "2",
"difficulty": 1,
"id": 10,
"question": "What is the colour of sky"
}
Response
{
"question": {
  "answer": "blue",
  "category": "2",
  "difficulty": 1,
  "id": 17,
  "question": "What is the colour of sky"
          },
"success": true
}

* GET /questions

Inserting a new question.
URI:- http://127.0.0.1:5000/questions
Response
{
"question": {
  "answer": "blue",
  "category": "2",
  "difficulty": 1,
  "id": 17,
  "question": "What is the colour of sky"
          },
"success": true
}

* POST /quizzes
URI:- http://127.0.0.1:5000/quizzes
JSON file format
{
    "quiz_category": {
        "type": "Science",
        "id": 1
    },
    "previous_questions": [1]
}
Response
{
    "question": {
        "answer": "Alexander Fleming",
        "category": 1,
        "difficulty": 3,
        "id": 21,
        "question": "Who discovered penicillin?"
    },
    "success": true
}
