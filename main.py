questions = [
"What is the name of the tallest mountain in the world?",
"Which country has the largest population in the world?",
"What is the name of the longest river in Africa?",
"What American city is the Golden Gate Bridge located in?",
"What is the capital of Mexico?",
"What is the name of the largest country in the world?",
"What U.S. state is home to no documented poisonous snakes?",
"What is the name of the largest ocean in the world?",
"What country are the Great Pyramids of Giza located in?",
"What is the name of the smallest country in the world?",
"What country has the most natural lakes?"
]
answers = [
"Mount Everest",
"China",
"The Nile River",
"San Francisco",
"Mexico City",
"Russia",
"Alaska",
"The Pacific Ocean",
"Egypt",
"The Vatican City",
"Canada"      
]



def askQuestions():
    score = 0
    cntr = 0
    ua=""
    correct = None
    for x in questions:
            print(x)
            ua = input("Answer: ")
            if (ua==answers[cntr]):
                print("Correct!!")
                correct = True
                score+=1
            else:
                print("Wrong!!")
                correct = False
            cntr+=1
    print(f"Score {score}/11")


     

askQuestions()