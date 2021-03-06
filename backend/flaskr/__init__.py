import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category, User

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    '''
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    '''
    CORS(app)

    '''
    @TODO: Use the after_request decorator to set Access-Control-Allow
    '''

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Autorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    '''
    @TODO: 
    Create an endpoint to handle GET requests 
    for all available categories.
    '''

    @app.route('/categories')
    def load_categories():
        categories_raw = Category.query.order_by(Category.id).all()
        categories = {category.id: category.type for category in categories_raw}
        users = [user.format() for user in User.query.order_by(User.id).all()]

        if len(categories) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'categories': categories,
            'total_categories': len(categories),
            'users': users
        })

    '''
    @TODO: 
    Create an endpoint to handle GET requests for questions, 
    including pagination (every 10 questions). 
    This endpoint should return a list of questions, 
    number of total questions, current category, categories. 
  
    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions. 
    '''

    @app.route('/questions')
    def load_questions():
        questions = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, questions)

        if len(current_questions) == 0:
            abort(404)

        categories_raw = Category.query.order_by(Category.id).all()
        categories = {category.id: category.type for category in categories_raw}

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(Question.query.all()),
            'current_category': None,
            'categories': categories
        })

    '''
    @TODO: 
    Create an endpoint to DELETE question using a question ID. 
  
    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page. 
    '''

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.filter(Question.id == question_id).one_or_none()

            if question is None:
                abort(404)

            question.delete()

            questions = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, questions)
            categories_raw = Category.query.order_by(Category.id).all()
            categories = {category.id: category.type for category in categories_raw}

            return jsonify({
                'success': True,
                'question_id': question_id,
                'questions': current_questions,
                'total_questions': len(Question.query.all()),
                'current_category': None,
                'categories': categories
            })

        except:
            abort(422)

    '''
    @TODO: 
    Create an endpoint to POST a new question, 
    which will require the question and answer text, 
    category, and difficulty score.
  
    TEST: When you submit a question on the "Add" tab, 
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.  
    '''

    @app.route('/questions', methods=['POST'])
    def add_question():
        data = request.get_json()
        question = data.get('question', '')
        answer = data.get('answer', '')
        category = data.get('category', '')
        difficulty = data.get('difficulty', '')
        rating = data.get('rating', '')

        try:
            new_question = Question(question, answer, category, difficulty, rating)
            if new_question is None:
                abort(404)
            new_question.insert()

            return jsonify({
                'success': True,
                'message': 'Question successfully created!',
                'question_id': new_question.id
            })

        except:
            abort(422)

    @app.route('/categories', methods=['POST'])
    def add_category():
        data = request.get_json()
        category_type = data.get('categoryType', '')

        try:
            category = Category(category_type)
            print(category.format())
            if category is None:
                abort(404)
            category.insert()

            return jsonify({
                'success': True,
                'message': 'Category successfully created!',
                'category_id': category.id
            })

        except:
            abort(422)

    '''
    @TODO: 
    Create a POST endpoint to get questions based on a search term. 
    It should return any questions for whom the search term 
    is a substring of the question. 
  
    TEST: Search by any phrase. The questions list will update to include 
    only question that include that string within their question. 
    Try using the word "title" to start. 
    '''

    @app.route('/questions/search', methods=['POST'])
    def search_questions():
        data = request.get_json()
        search_term = data.get('searchTerm', '')

        if len(search_term) == 0:
            abort(404)

        try:
            questions = Question.query.filter(Question.question.ilike(f'%{search_term}%')).all()

            return jsonify({
                'success': True,
                'questions': [question.format() for question in questions],
                'total_questions': len(Question.query.all()),
                'current_category': None
            })

        except:
            abort(422)

    '''
    @TODO: 
    Create a GET endpoint to get questions based on category. 
  
    TEST: In the "List" tab / main screen, clicking on one of the 
    categories in the left column will cause only questions of that 
    category to be shown. 
    '''

    @app.route('/categories/<int:category_id>/questions')
    def load_questions_by_category(category_id):
        questions = Question.query.filter(Question.category == category_id).all()
        current_questions = paginate_questions(request, questions)

        if len(current_questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(Question.query.all()),
            'current_category': Category.query.filter(Category.id == category_id).first().format()
        })

    '''
    @TODO: 
    Create a POST endpoint to get questions to play the quiz. 
    This endpoint should take category and previous question parameters 
    and return a random questions within the given category, 
    if provided, and that is not one of the previous questions. 
  
    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not. 
    '''

    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
        try:
            data = request.get_json()
            previous_questions = data.get('previous_questions', '')
            quiz_category = data.get('quiz_category', '')
            user = data.get('user', '')
            number_guess = data.get('numGuess', '')

            total_score = 0

            if user != '' and user is not None:
                current_user = User.query.filter(User.id == user).one_or_none()
                current_user.score = current_user.score + int(number_guess)
                current_user.update()
                print(current_user.score)
                total_score = current_user.score

            if quiz_category['id'] == 0:
                questions = Question.query.filter(Question.id.notin_(previous_questions)).all()
            else:
                questions = Question.query.filter(Question.category == quiz_category['id']).filter(
                    Question.id.notin_(previous_questions)).all()

            question = questions[random.randrange(len(questions))].format() if len(questions) > 0 else None

            return jsonify({
                'success': True,
                'question': question,
                'previous_questions': previous_questions,
                'user': user,
                'numTotal': total_score
            })
        except:
            abort(404)

    '''
    @TODO: 
    Create error handlers for all expected errors 
    including 404 and 422. 
    '''

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not Found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable Error"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    return app
