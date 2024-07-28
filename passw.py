import random

lst2=[]
for i in range(30,123):
    lst2.append(chr(i))
    try:
        lst2.append(chr(i).capitalize())
    except:
        pass

user_n=int(input("Enter the Number of passwords u want : "))
user_l=int(input("Enter the length of those passwords : "))

lsst=[]
for i in range(user_n):
    strr=""
    for j in range(user_l):
    
        strr=strr+random.choice(lst2)
    lsst.append(strr)

print(lsst)