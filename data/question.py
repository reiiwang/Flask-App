Contexts = [
    {
        "Evidence": "NTU is a good school",
        "Answer": "He likes it"
    },
    {
        "Evidence": "NTU is a bad school",
        "Answer": "He don't like it"
    },
    {
        "Evidence": "I like NTU\nI like coffee",
        "Answer": "I like studying"
    }
]

questions = [
    {
        "text": "Question 1: Correct?",
        "options": [1,2,3,4]
    },
    {
        "text": "Question 2: Fluent?",
        "options": [1,2,3,4]
    },
    {
        "text": "Question 3: Cover all evidence?",
        "options": [1,2,3,4]
    },
]

def get_contexts():
    return Contexts

def get_questions():
    return questions