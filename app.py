from flask import Flask, render_template, request, redirect, url_for
from data.question import get_questions

questions = get_questions()

app = Flask(__name__)

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
        
        # Here you could save the responses to a database
        # For this example, we'll just print them
        print(responses)
        # save to file
        with open('responses.txt', 'a') as f:
            f.write(str(responses) + '\n')
        
        # You could also pass the responses to a template to display them
        return render_template('results.html', responses=responses)
    
    # If not a POST request, redirect to the index
    # return redirect(url_for('index'))
    return redirect(url_for('lastpage'))

if __name__ == '__main__':
    app.run(debug=True)