from flask import Flask, render_template, request, redirect, url_for
from data.question import get_questions
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import json

questions = get_questions()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///form.db"
db = SQLAlchemy(app)


class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    response = db.Column(db.String(500), nullable=False)
    q1 = db.Column(db.String(500), nullable=False)
    q2 = db.Column(db.String(500), nullable=False)
    q3 = db.Column(db.String(500), nullable=False)
    q4 = db.Column(db.String(500), nullable=False)
    time = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    def __repr__(self):
        return f"Response('{self.response}')"
    
    @property
    def as_json(self):
        return {
            'response': self.response
        }

if not os.path.exists('form.db'):
    with app.app_context():
        db.create_all()

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/lastpage')
def lastpage():
    return render_template('lastpage.html', title='Thank You')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        responses = {}
        for i in range(1, len(questions) + 1):
            question_key = f'q{i}'
            if question_key in request.form:
                responses[question_key] = request.form[question_key]
            else:
                responses[question_key] = 'Not answered'
        
        response = Response(response=json.dumps(responses))
        response.q1 = responses['q1']
        response.q2 = responses['q2']
        response.q3 = responses['q3']
        response.q4 = responses['q4']
        db.session.add(response)
        db.session.commit()

        # Here you could save the responses to a database
        # For this example, we'll just print them
        print(responses)
        # save to file
        # with open('responses.txt', 'a') as f:
        #     f.write(str(responses) + '\n')
        
        # You could also pass the responses to a template to display them
        return render_template('results.html', responses=responses)
    
    # If not a POST request, redirect to the index
    # return redirect(url_for('index'))
    return redirect(url_for('lastpage'))

if __name__ == '__main__':
    app.run(debug=True)