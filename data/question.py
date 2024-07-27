Contexts = [
    {
        "Question": "How can you treat symptoms of de Quervain's disease? 如何治療奎文氏症的症狀？",
        "Evidence": [" \
        1. You'll start with over-the-counter pain relievers like ibuprofen or naproxen to ease the swelling. \
        你可以先使用布洛芬或萘普生等非處方止痛藥來緩解腫脹。",
        "2. But try these methods at home to feel better and keep your thumb healthy: Ice the area to ease inflammation. \
        但是在家嘗試這些方法可以感覺更好並保持拇指健康：冰敷該區域以緩解發炎。"],
        "Answer": " \
        Over-the-counter pain relievers like ibuprofen or naproxen can be used to ease the swelling, and icing the area can help to reduce inflammation. 布洛芬或萘普生等非處方止痛藥可用於緩解腫脹，冰敷患處有助於減輕發炎。"
    },
    {
        "Question": "What are the symptoms of tachycardia? 心跳過速有哪些症狀？",   
        "Evidence": ["1. No matter which type of tachycardia you have, you may feel: Dizziness Lightheadedness Shortness of breath Chest pain Heart palpitations In extreme cases, you could become unconscious or go into cardiac arrest. 無論您患有哪種類型的心動過速，您都可能會感到： 頭暈 頭暈 呼吸短促 胸痛 心悸 在極端情況下，您可能會失去知覺或心臟驟停。",
                     "2. But sometimes, a super-fast heart rate causes no symptoms at all. 但有時，超快的心率根本不會引起任何症狀。"],
        "Answer": "Symptoms of tachycardia may include dizziness, lightheadedness, shortness of breath, chest pain, heart palpitations, and in extreme cases, unconsciousness or cardiac arrest. However, sometimes a super-fast heart rate causes no symptoms at all. 心搏過速的症狀可能包括頭暈、頭暈、氣短、胸痛、心悸，在極端情況下，甚至會出現意識不清或心臟停止。然而，有時超快的心率根本不會引起任何症狀。"
    },
    {
        "Question": "How can pets cause allergy problems in bedrooms? 寵物如何在臥室引起過敏問題？",
        "Evidence": ["1. But dander, saliva, and pee from furry animals can carry allergens. 但毛茸茸的動物的皮屑、唾液和尿液可能帶有過敏原。",
                     "2. Ideally, your dog or cat should sleep somewhere else. 理想情況下，您的狗或貓應該睡在其他地方。",
                     "3. If not, do your best to reduce dander. 如果沒有，請盡力減少皮屑。",
                     "4. For example, vacuum more often. 例如，更頻繁地吸塵。"],
        "Answer": "Pets can cause allergy problems in bedrooms because their dander, saliva, and pee can carry allergens. Ideally, pets should sleep in a different room. If this is not possible, try to reduce dander by vacuuming more often. 寵物在臥室可能會引起過敏問題，因為它們的皮屑、唾液和尿液可能帶有過敏原。理想情況下，寵物應該睡在不同的房間。如果無法做到這一點，請嘗試更頻繁地吸塵以減少皮屑。"
    }
]

questions = [
    {
        "text": "Question 1: 答案(Answer)是否只包含證據(Evidence)中提到的資訊? (亦即是否有超出證據的資訊)",
        "options": ["1: 完全符合 100%", "2: 大部分符合 >50%", "3: 少部分符合 <=50%", "4: 完全不符合 0%"],
        "options_note": ["完全符合 100% (答案完全依循證據中的資訊，沒有包含任何超出證據的額外資訊或解釋。換言之，答案提及的資訊都可以在證據中找到)",
                         "大部分符合 >50% (答案大部分依循證據中的資訊，但可能加入了一些輔助資訊或解釋。這些輔助資訊並不改變證據的主要含義，但可能增加了一些背景或細節。)",
                         "部分符合 <50% (答案只有部分根據證據中的資訊，其他大部分內容是由LLM加入的額外資訊或解釋，這些資訊可能是證據的延伸。)",
                         "完全不符合 0% (答案完全沒有根據證據中的資訊，內容都是額外資訊、錯誤資訊或與證據無關的內容。)"]
    },
    {
        "text": "Question 2: 答案(Answer)是否涵蓋所有證據(Evidence)中提及的資訊?",
        "options": ["1: 完全涵蓋 100%","2: 大部分涵蓋 >50%","3: 部分涵蓋 <50%", "4: 完全未涵蓋 0%"],
        "options_note": ["完全涵蓋 100% (答案內容涵蓋了證據中的每個句子所提及的重要資訊，這些句子在答案中可能經過重寫、精簡、總結，但意思不變。)",
                            "大部分涵蓋 >50% (答案內容涵蓋了證據中的大部分片段的重要資訊，但可能遺漏了某些片段的資訊)",
                            "部分涵蓋 <50% (答案中只有一部分重要資訊被涵蓋，大部分證據片段並未在答案被提及。)",
                            "完全未涵蓋 0% (答案中完全沒有涵蓋證據中的任何句子所提及的重要資訊。)"]
    },
    {
        "text": "Question 3: 答案(Answer)的表達是否通順且流利?",
        "options": ["1: 非常通順 100%","2: 較為通順 >50%","3: 不太通順 <50%", "5: 非常不通順 0%"],
        "options_note": ["非常通順 100% (答案表達流暢、通順。)",
                            "較為通順 >50% (答案表達大致流暢，但可能有少量語法錯誤或不自然的表達方式，但不影響整體理解。)",
                            "不太通順 <50% (答案表達不太流暢，有較多的語法錯誤或不自然的地方，影響了理解。)",
                            "非常不通順 0% (答案表達不流暢，具有語法錯誤與不自然的表達，難以理解。)"]
    },
    {
        "text": "Question 4: 答案 (Answer) 的內容是否正確?",
        "options": ["1: 完全正確 100%","2: 大部分正確 >50%","3: 部分正確 <50%", "4: 完全不正確 0%"],
        "options_note": ["完全正確 100% (不考慮答案是否符合第一題與第二題的情況下，基於問題與證據，答案中的資訊正確，與證據或已知事實一致。)",
                         "大部分正確 >50% (不考慮答案是否符合第一題與第二題的情況下，基於問題與證據，答案中的大部分資訊是正確的，但可能有一些小錯誤或不準確的地方。)",
                         "3: 部分正確 <50% (不考慮答案是否符合第一題與第二題的情況下，基於問題與證據，答案中只有一部分資訊是正確的，大部分內容有誤。)",
                         "4: 完全不正確 0% (不考慮答案是否符合第一題與第二題的情況下，基於問題與證據，答案中的所有資訊都是錯誤的，沒有一部分是正確的。)"]
    }
]

def get_contexts():
    return Contexts

def get_questions():
    return questions
