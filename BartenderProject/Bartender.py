import random
import re

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

#print(questions)
#print(ingredients)

def chooseQuestion(q):
    #print(list(questions))
    #print(random.choice(list(questions.keys())))
    #print(random.choice(list(questions.items())))
    if q is None:
        return random.choice(list(questions.items()))
    else:
        return random.choice([x for x in list(questions.items()) if x != q])

def chooseIngredient(q_key):
    #print(ingredients.get(q_key))
    #print(random.choice(list(ingredients.get(q_key))))
    return random.choice(list(ingredients.get(q_key)))


def main():
    my_question = None
    while True:
        my_question = chooseQuestion(my_question)
        #print(my_question)
        your_anwer = input(my_question[1])
        if re.compile('^(yes|y|1)$').match(str(your_anwer).lower()):
           print("Yes, today we have: ", chooseIngredient(my_question[0]))

        print("")
        print("Thank you!!!")
        print("_______________________^-^______________________")
        print("")

if __name__ == '__main__':
    main()