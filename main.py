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
counter=0


def quiz (ques, ans):
      global counter
      score=0
      for x in ques:
            userinput = input(f"{x}(user input - type the answer): ") #The user inputs an answer to the question
            score = compareStrings(userinput, ans[counter], score)
            counter+=1
      print(f"Your score is {score}/11 ")  


def compareStrings(str1,str2,scr):
      finished = False
      while not finished:
            global counter
            if str1.lower() == str2.lower():
                  print("Your answer is correct!!")
                  scr+=1
            else:
                  print(f"Your answer is wrong!! The correct answer was {answers[counter]}")
            finished = True if scr < 11 else False
      return scr
quiz(questions,answers)

