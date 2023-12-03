#imported the random function
import random

question1 = """Question 1: What is Python primarily used for?
A) Cooking recipes
B) Writing letters
C) Computer programming
D) Gardening """

question2 = """Question 2: What is a PEP 8?
A) A type of soda
B) A style guide for Python code
C) A Python mascot
D) A popular Python library"""

question3 = """Question 3: What does a virtual environment help with in Python?
A) Virtual gaming
B) Isolating germs
C) Keeping code organized
D) Separating pets"""

question4 = """Question 4: How do you read a book in Python?
A) With a magnifying glass
B) By using the open() function
C) By shaking it
D) By eating it"""

question5 = """Question 5: What is the if __name__ == "__main__": statement used for?
A) Checking the weather
B) Defining a Python function
C) Writing a love letter
D) Running a Python script"""

question6 = """Question 6: What's the difference between a list and a tuple?
A) Lists are for shopping, tuples are for cooking
B) Lists are spelled with four letters, tuples with five
C) Lists can change, tuples cannot
D) Lists are for cats, tuples are for dogs"""

question7 = """Question 7: How do you make a sandwich in Python?
A) With a magic spell
B) By using the def keyword
C) With peanut butter and jelly
D) By writing a nove"""

question8 = """Question 8: What does the __init__ method do in a Python class?
A) Starts a Python script
B) Initializes object attributes
C) Sends emails
D) Solves math problems"""

question9 = """Question 9: What's a lambda function in Python?
A) A type of food
B) A fancy word for "function"
C) An anonymous, short function
D) A Python mascot"""

question10 = """Question 10: How do you catch a fish in Python?
A) With a fishing rod
B) By using try and except
C) By writing a letter to the fish
D) By telling a fish joke"""

question11 = """Question11: What is a dictionary comprehension in Python?
A) A way to write love letters
B) A recipe for making dictionaries
C) A shortcut for creating dictionaries
D) A dictionary for learning words"""

question12 = """Question 12: How do you remove duplicates from a list in Python?
A) With a magic wand
B) By using a dictionary
C) By using a set
D) By eating ice cream"""

question13 = """Question 13: What's the super() function used for in Python?
A) Making superheroes
B) Calling a method from the parent class
C) Cooking dinner
D) Solving puzzle"""

question14 = """Question 14: What is the Global Interpreter Lock (GIL) in Python?
A) A safety feature in a car
B) A type of lock for doors
C) A lock that allows only one thread to execute in Python
D) A secret code"""

question15 = """Question 15: How do you test if a lightbulb is working in Python?
A) By using a unittest
B) By flipping the switch
C) By sending an email
D) By using a flashligh"""

#created the dictionary
questions = {question1:"C",question2:"B",question3:"C",question4:"B",question5:"D",
             question6:"C",question7:"B",question8:"B",question9:"C",question10:"B",
             question11:"C",question12:"C",question13:"B",question14:"C",question15:"A"}


#firstly create a function
def Assignment_quiz():

    #outer loop to allow multiple users
    users = []
    
    while True:
        
        name = input("Please enter your name:\n")

        #to randomise the question
        random_questions = list(questions.items())
        random.shuffle(random_questions)
        number_of_questions = int(input("Hi " + name + " Welcome to my quiz game :)\n" "How many questions do you want to answer, choose from (1 - 15)?\n"))
        
        if 1 <= number_of_questions <= 15:
        
        #we loop through the questions
            score = 0
        
    
            for i in range(number_of_questions):
                question, correct_answer = random_questions[i]
                print(question)

                
                answer = input("Please input your answer by choosing from (A,B,C,D):\n")

            
            #iterrated the score to plus 1 if the user got the question correctly.
        
                try:
                    if answer.upper() == questions[question]:
                        print("correct! you got 1 point")
                        score = score +1
                    else:   
                        print("sorry! wrong answer")
                except KeyError:
                    print("Invalid answer please proceed to the next question")

            #store user informatio (name and score) in the users list
            users.append((name, score,))

            print("Your total score is: " + str(score))
            print(f"You got {(score/len(questions))* 100:.2f}%")
            

            exit_quiz = input("Is any other person interested in playing (yes or no):\n")
            if exit_quiz.upper() == "NO":
                break
            
        else:
            print("Please choose a number from 1 to 15")
        

    if users:
        #calculate the Average and the highest scoring user

        average_score = sum(user[1] for user in users) / len(users)
        print(f"The average score across all quiz takers is: {average_score:.2f}%")

        highest_score_user = max(users, key=lambda user: user[1])
        print(f"The User with the highest score is: {highest_score_user[0]} with a score of {highest_score_user[1]} points")

    #call the function

Assignment_quiz ()
