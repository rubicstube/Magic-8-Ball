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

def display_response(response):
    print("\n🔮 The Magic 8-Ball says:",response,"\n")
    
