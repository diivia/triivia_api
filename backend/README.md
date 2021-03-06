# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

## Error Handling
Errors returned as JSON objects in the following format
```
{
    "success": False,
    "error": 400,
    "message": "bad request"    
}
```
The API will return 3 error types when request fails:
```
400: Bad request
401: Not Found
422: Unprocessable Error
```

## Endpoints
```
GET '/categories' - returns all categories and users
GET '/questions?page=<page_number>' - returns paginated questions (10 questions per page)
DELETE '/questions/<question_id>' - deletes question
POST '/questions' - adds new question
POST '/categories' - adds new category
POST '/questions/search' - returnes all questions by given search criteria
GET '/categories/<category_id>/questions' - returnes all question of one selected category or all questions 
POST /quizzes - returnes random question from selected category, previously selected question excluded
```


##### GET '/categories'
- Fetches a dictionary of all categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- curl http://127.0.0.1:5000/categories
- Example response:
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports", 
    "7": "Misc", 
    "8": "User"
  }, 
  "success": true, 
  "total_categories": 8, 
  "users": [
    {
      "id": 1, 
      "name": "Scientist", 
      "score": 4
    }, 
    {
      "id": 2, 
      "name": "Artist", 
      "score": 30
    }, 
    {
      "id": 3, 
      "name": "Geography student", 
      "score": 3
    }, 
    {
      "id": 4, 
      "name": "History teacher", 
      "score": 0
    }, 
    {
      "id": 5, 
      "name": "Entertainment artist", 
      "score": 0
    }, 
    {
      "id": 6, 
      "name": "Sports designer", 
      "score": 0
    }
  ]
}
```

##### GET '/questions?page=<page_number>'
- Fetches a list of all questions
- Request Arguments: page_number - integer, optional
- curl http://127.0.0.1:5000/questions?page=1
- Example response:
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports", 
    "7": "Misc", 
    "8": "User"
  }, 
  "current_category": null, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?", 
      "rating": 4
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?", 
      "rating": 4
    }, 
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?", 
      "rating": 4
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?", 
      "rating": 4
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?", 
      "rating": 4
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?", 
      "rating": 4
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?", 
      "rating": 4
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?", 
      "rating": 4
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?", 
      "rating": 4
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?", 
      "rating": 4
    }
  ], 
  "success": true, 
  "total_questions": 18
}
```

##### DELETE '/questions/<question_id>'
- Deletes question by ID 
- Request Arguments: question_id - integer
- curl -X DELETE http://127.0.0.1:5000/questions/13
- Example response:
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports", 
    "7": "Misc", 
    "8": "User"
  }, 
  "current_category": null, 
  "question_id": 12, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?", 
      "rating": 4
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?", 
      "rating": 4
    }, 
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?", 
      "rating": 4
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?", 
      "rating": 4
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?", 
      "rating": 4
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?", 
      "rating": 4
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?", 
      "rating": 4
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?", 
      "rating": 4
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?", 
      "rating": 4
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?", 
      "rating": 4
    }
  ], 
  "success": true, 
  "total_questions": 17
}
```
##### POST '/categories'
- Adds a new question
- Request Arguments: {"question": String, "answer": String, "category": Integer, "difficulty": Integer}
- curl -X POST -H "Content-Type: application/json" -d '{"categoryType": "qwerty"}' http://127.0.0.1:5000/categories
- Example response:
```
{
  "category_id": 8, 
  "message": "Category successfully created!", 
  "success": true
}
```

##### POST '/questions'
- Adds a new category
- Request Arguments: {"categoryType": String}
- curl -X POST -H "Content-Type: application/json" -d '{"question": "qwerty", "answer": "qwerty", "category": "1", "difficulty": "1", "rating": "1"}' http://127.0.0.1:5000/questions
- Example response:
```
{
  "message": "Question successfully created!", 
  "question_id": 34, 
  "success": true
}
```

##### POST '/questions/search'
- Fetches a list of questions by search tearm
- Request Arguments: search_term, string
- curl -X POST -H "Content-Type: application/json" -d '{"searchTerm": "Hematology"}' http://127.0.0.1:5000/questions/search
- Example response:
```
{
  "current_category": null, 
  "questions": [
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?", 
      "rating": 4
    }
  ], 
  "success": true, 
  "total_questions": 18
}
```
##### GET '/categories/<category_id>/questions'
- Fetches a list of all questions for some category
- Request Arguments: category_id, integer
- curl -X GET http://127.0.0.1:5000/categories/2/questions
- Example response:
```
{
  "current_category": {
    "id": 2, 
    "type": "Art"
  }, 
  "questions": [
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?", 
      "rating": 4
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?", 
      "rating": 4
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?", 
      "rating": 4
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?", 
      "rating": 4
    }
  ], 
  "success": true, 
  "total_questions": 18
}
```

##### POST '/quizzes'
- Fetches a random question from any selected category. Previously asked question excluded from selection. 
- Request Arguments: {previous_questions: [Integer, Integer, ...], quiz_category: {'type': String, 'id': Integer}}
- curl -X POST -H "Content-Type: application/json" -d '{"previous_questions": [22, 36, 20], "quiz_category": {"type": "Science", "id": "1"}, "user":1, "numGuess": 1}' http://127.0.0.1:5000/quizzes
- Example response:
```
{
  "numTotal": 6, 
  "previous_questions": [
    22, 
    36, 
    20
  ], 
  "question": {
    "answer": "qwerty", 
    "category": 1, 
    "difficulty": 1, 
    "id": 24, 
    "question": "qwerty", 
    "rating": 1
  }, 
  "success": true, 
  "user": 1
}
```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```