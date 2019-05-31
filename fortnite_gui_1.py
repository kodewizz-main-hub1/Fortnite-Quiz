import time
import random
import tkinter

start = time.time()

mainWindow = tkinter.Tk()
mainWindow.title("Fortnite quiz")
mainWindow.geometry('648x480-8-200')

sheild_questions = 'Sheild questions'
gun_questions = 'Gun Questions'
device_questions = 'Devices Questions'

print("Welcome to the fortnite quiz.")

questions = [sheild_questions, gun_questions, device_questions]

quiz = {sheild_questions: [("Do big pots give u 50 shield?", True),
                           ("Do characters start the game with 200 health and sheild combined?", False),
                           ("Do u get 25 sheild from minis?", True)],

        gun_questions: [("Are machine guns better than snipers.", True),
                        ("Are there wrappers for guns.", True),
                        ("blue guns are the best type False"), False],

        device_questions: [("Gunners are in every game mode.", False),
                           ("Ballons pop when too high up in the air.", True),
                           ("Suraj is the best player at fortnite(not true)#trolling 101", True)]
        }


qRight = 0

def get_quiz_choice():
    while True:
        try:
            quiz_number = int(input(
                'Choose the quiz you like 1 for {} 2 for {} 3 for {} Your choice:'.format(sheild_questions,
                                                                                          gun_questions,
                                                                                          device_questions)))
        except ValueError:
            print("Not a number, please try again")
        else:
            return quiz_number


def get_answer(question, correct_answer):
    global qRight
    while True:
        try:
            print("Q: {}".format(question))
            answer = int(input("1 for True 0 for False Your answer: "))
        except ValueError:
            print ("Not a number, please try again")
        else:
            if answer is not 0 and answer is not 1:
                print ("Invalid value, please try again")
            elif bool(answer) is correct_answer:
                qRight += 1
                return "Correct"
            else:
                return "Incorrect"


choice = get_quiz_choice()
quiz_name = questions[choice - 1]
print ("You chose the {}".format(quiz_name))
quiz_questions = quiz[quiz_name]
for q in (quiz_questions):
    print( "Your answer is: {}".format(str(get_answer(q[0], q[1]))))

print("You got {} questions right".format(qRight))

end = time.time()
print(end - start)