import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass
    # || DONE || 
    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    #Categories
    def test_get_paginated_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])


    def test_404_if_category_does_not_exist(self):
        res = self.client().delete('/categories/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found!')

    
    # Questions
    def test_get_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
    
    def test_404_sent_requesting_beyond_valid_ques_page(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found!')
    
    def test_delete_question(self):
        res = self.client().delete('/questions/13')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'],13)

    
    def test_404_if_question_does_not_exist_delete(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)

        question = Question.query.filter(Question.id == 1000).one_or_none()

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable')

    def test_422_if_question_does_not_exist(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable')

    def test_get_question_search_with_results(self):
        res = self.client().post('/questions/search', json={'searchTerm': 'tim'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_post_new_question(self):
        res = self.client().post('/questions', json={"answer": "blue","category": "2","difficulty": 1,"question": "What is the colour of sky"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_post_new_question(self):
        res = self.client().post('/questions', json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable')



    #Quiezz
    def test_trivia_quizz(self):
        res = self.client().post('/quizzes', json={"quiz_category": {"type": "Science","id": 1},"previous_questions": [1]})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_404_trivia_quizz(self):
        res = self.client().post('/quizzes', json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable')

        pass

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()