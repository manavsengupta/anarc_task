import random

lst=["Rock","Paper","Scissor"]
computer_decision=random.choice(lst)


user_decision=eval(input("Rock(0)\nPaper(1)\nScissor(2): "))

if(lst.index(computer_decision)+1==3):
    r=0
else:
    r=lst.index(computer_decision)+1

if(user_decision==r):
    result="You Win!"
elif(lst[user_decision]!=computer_decision):
    result="You Lose!"
else:
    result="Draw!"
print(f"\n The computer chose {computer_decision}, thus {result}")