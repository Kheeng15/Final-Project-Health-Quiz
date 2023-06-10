import time
from os import system 

line = ("----------------------------------------------------------------------------------------------------------")
user_options = ["A", "B", "C", "D", "T", "F"]

# Print a welcome note
print("WELCOME TO HEALTH_TIDBIT QUIZ GAME!")
print("")
playing = input(("Would you like to test your knowledge on how well you know Diabetes?(yes/no) "))

if playing.lower() != "yes":
    print("Thank you and see you next time!")
    quit()
      
print("Great! Let's play")
time.sleep(1)

# A countdown timer that prepares users before they begin the quiz 
for x in range(5, 0, -1):
        seconds = x % 60
        system("clear")
        print("The game start in...", end=" ")
        print(f"{seconds:2}")
        time.sleep(1)

system("clear")

print("START!\n")
print("Your time starts now!")

# Defining some functions; that starts a new game, checks the answers, displays the scores, and prompt a user if he/she wants to play again
def new_game():
    time_start  = time.time()
    guesses = []
    correct_guesses  = 0
    question_num = 1
    
    for key in questions:
        print(line)
        
        print(key)
        for q in options[question_num - 1]:
            print (q)
        while True:
            guess = input("Enter (A, B, C, D, T or F): ")
            guess = guess.upper()
            
            if guess in user_options:
                guesses.append(guess)
                break
            else:
                print("Input not valid")
                continue
                
        correct_guesses += check_answer(questions.get(key), guess)              
        question_num += 1
        time_stop = time.time()
        time_taken = time_stop - time_start

        system("clear")  
    display_score(correct_guesses, guesses, time_taken)
    
    
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("INCORRECT")
        return 0

def display_score(correct_guesses, guesses, time_taken):
    system("clear")
    print(line)
    print("RESULTS")
    print(line)
    
    print("Answers: ", end="")
    for q in questions:
        print(questions.get(q), end=" ")
    print()
    
    
    print("Guesses: ", end="")
    for q in guesses:
        print(q, end=" ")
        
    score = int((correct_guesses/len(questions)) * 100)
    print("\nYour score is: " +str(score)+"%")
    if time_taken <= 60:
        print(f"\nYour time taken is: {time_taken:.2f} secs")
    elif time_taken > 60:
        print(f"\nYour time taken is: {time_taken/60:.2f} min")
    
    
    
    print("Remarks: ", end="")
    if score > 69:
        print("Excellent! You are on fire!")
    elif score >= 50:
        print("Good! But you can do better.")
    elif score > 20 and score < 50:
        print("Not so good, you can do better.")
    else:
        print("Too poor, you can do much better.")
        
    
def play_again():
    print("")
    while True:
        response = input("Do you want to play again?(yes/no): ")
        response = response.upper()
        
        if response == "YES":
            return True
        elif response == "NO":
            return False
        else:
            print("Choose either yes or no")
            continue

# Using dictionaries to store the questions and the correct answers
questions = {"1. All are the three MAIN types of Diabetes except? ": "A",
             "2. Which of the following hormones acts like a key to let the blood sugar into your bodys cells for use as energy.": "B",
             "3. Which of the following types of Diabetes is not caused by diet or lifestyle choices?": "A",
             "4. People with diabetes should not eat fruit because they are sweet? True or False?(T/F) ": "F",
             "5. Type 1 diabetes is also called? ": "C",
             "6. Type 1 diabetes occurs when? ": "B",
             "7. Type 1 Diabetes can be prevented? True or False?(T/F) ": "F",
             "8. Which of the following types of Diabetes can be prevented by healthy lifestyle? ": "C",
             "9. Type 2 Diabetes occurs when? ": "A",
             "10. Trauma to the pancreas can cause Diabetes? True or False?(T/F) ": "T",
             "11. Excessive hunger even after eating can be a sign of Diabetes? True or False?(T/F) ": "T",
             "12. Diabetes mellitus refers to: ": "A",
             "13. Types of Diabetes are: ": "B",
             "14. Which type of Diabetes is most common? ": "B",
             "15. With the following symptoms \n ~ have a family history of diabetes \n ~ 45 years or older \n ~ overweight \n ~ physically inactive/lack a regular excercise routine \n ~ have a high blood pressure \n Am I at risk of developing Type 2 Diabetes? ": "A",
             "16. How can I manage my Diabetes better? ": "A"
            }

# Using lists in list to store the possible answers to each question
options = [["a) Type 1", "b) Type 2" ,"c) Type 3", "d) Gestational Diabetes"],
           ["a) Glucagon" ,"b) Insulin", "c) Adrenaline", "d) Antidiuretic hormone"],
           ["a) Type 1" ,"b) Type 2", "c) Type 4"],
           ["T", "F"],
           ["a) Geriatric Diabetes" ,"b) Gestational Diabetes" ,"c) Juvenile Diabetes"],
           ["a) your body still produces insulin, but it does not make enough of it or it does not use it efficiently. It is the most common form of diabetes.",
           "b) your body is no longer able to produce insulin.", "c) occurs during pregnancy"],
           ["T", "F"],
           ["a) Type 1", "b) Type 4", "c) Type 2"],
           ["a) your body still produces insulin, but it does not make enough of it or it does not use it efficiently. It is the most common form of diabetes.",
           "b) your body is no longer able to produce insulin.", "c) occurs during pregnancy"],
           ["T", "F"],
           ["T", "F"],
           ["a) A group of diseases that affect how the body uses blood sugar(glucose)", "b) Glucose in our muscles and tissues", "c) Brains main source of food"],
           ["a) Type 0 only", "b) Type 1 and Type 2", "c) Type 0 and Type 1"],
           ["a) Type 1", "b) Type 2", "c) Both"],
           ["a) Yes", "b) Not sure", "c) No"],
           ["a) ~ keep close watch over your blood glucose level\n ~ pay attention to your blood pressure - adjust diet anad lifestyle choices to help lower it\n ~ watch chholesterol levels\n ~ maintain the health of your kidneys - consult your doctor or nephrologist to have a microalbumin test at least once every year\n ~ get your foot examined by aprofessional once a year", "b) Ignore it", "c) curse self"]
    
          ]

new_game()

# A loop that asks users if they want to play again
while play_again():
    new_game()
    
print("See you next time, never forget to value your health")



