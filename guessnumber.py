import random

def crack_pass(passw):
    trial=random.randint(0,100)
    if(trial==passw):
        return trial
    else:
        return crack_pass(passw)

user_input=int(input("\n\nEnter the Number: (till 100): "))
print("\nCracking Password ......\n")
print(f"The Cracked Pass is : {crack_pass(user_input)}")