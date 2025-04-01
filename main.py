#Both of us ->
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

# Nare->
def question (qList,aList):
    counter = 0
    score = 0
    for i in qList: 
           ui = input(f"{i}: ")
           compareStrings(ui,aList[counter],score)   
           counter+=1
    print(f"You got {score}/{len(aList)}")

#Uri->
def compareStrings(str1,str2,scr):
      if str1.lower() == str2.lower():
           print("Your answer is correct!!")
           scr+=1
      else:
            print("Your answer is wrong!!")
    
question (questions,answers)