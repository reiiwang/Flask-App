Contexts = [
    {
        "Evidence": "Evidence 1",
        "Answer": "Answer 1"
    },
    {
        "Evidence": "Evidence 2",
        "Answer": "Answer 2"
    },
    {
        "Evidence": "Evidence 3",
        "Answer": "Answer 3"
    }
]

questions = [
    {
        "text": "Question 1: Correct?",
        "options": ["Red", "Blue", "Green", "Yellow"]
    },
    {
        "text": "Question 2: Fluent?",
        "options": ["Spring", "Summer", "Autumn", "Winter"]
    },
    {
        "text": "Question 3: Cover all evidence?",
        "options": ["Car", "Bicycle", "Public Transport", "Walking"]
    },
]

def get_contexts():
    return Contexts

def get_questions():
    return questions