from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = [
    {
        "text": "Question 1: What is your favorite color?",
        "options": ["Red", "Blue", "Green", "Yellow"]
    },
    {
        "text": "Question 2: Which season do you prefer?",
        "options": ["Spring", "Summer", "Autumn", "Winter"]
    },
    {
        "text": "Question 3: What's your preferred mode of transportation?",
        "options": ["Car", "Bicycle", "Public Transport", "Walking"]
    },
    {
        "text": "Question 4: Which cuisine do you enjoy the most?",
        "options": ["Italian", "Chinese", "Mexican", "Indian"]
    }
]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

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
        
        # You could also pass the responses to a template to display them
        return render_template('results.html', responses=responses)
    
    # If not a POST request, redirect to the index
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)