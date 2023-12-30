import random

user_cho=int(input("what do you choice? rock: 0 ,paper: 1 or scissors: 2"))
pc_cho=random.randint(0,2)
print(f"pc choice {pc_cho}")

if user_cho==0:
    if pc_cho==0:
        print("tie")
    elif pc_cho==1:
        print("pc win")
    elif pc_cho==2:
        print("user win")
if user_cho==1:
    if pc_cho==0:
        print("user win")
    elif pc_cho==1:
        print("tie")
    elif pc_cho==2:
        print("pc win")
if user_cho==2:
    if pc_cho == 0:
        print("pc win")
    elif pc_cho == 1:
        print("user win")
    elif pc_cho == 2:
        print("tie")


