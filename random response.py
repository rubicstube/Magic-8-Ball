import random 

responses=[
    "yes definitly",
    " no not now",
    " maybe later",
    " certain ",
    "very doubtful",
    " outlook is good",
    "bett not tell you know",
    "concentrate and ask again",
]

def get_random_response():
    return random.choice(responses)