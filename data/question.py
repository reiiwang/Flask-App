Contexts = [
    {
        "Evidence": "<hr>1. You'll start with over-the-counter pain relievers like ibuprofen or naproxen to ease the swelling. 你可以先使用布洛芬或萘普生等非處方止痛藥來緩解腫脹。<hr>2. But try these methods at home to feel better and keep your thumb healthy: Ice the area to ease inflammation. 但是在家嘗試這些方法可以感覺更好並保持拇指健康：冰敷該區域以緩解發炎。",
        "Answer": "Over-the-counter pain relievers like ibuprofen or naproxen can be used to ease the swelling, and icing the area can help to reduce inflammation. 布洛芬或萘普生等非處方止痛藥可用於緩解腫脹，冰敷患處有助於減輕發炎。"
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
