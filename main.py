'''
1 for snake 
-1 for water 
0 for gun
'''

import random
computer = random.choice([-1,0,1])

yourstr = input("Enter your choice : ")
youDict = { 
     "s" : 1 , 
     "w" : -1 ,
     "g" : 0
    }
reverseDict = {
     1:"Snake",
    -1:"water",
     0:"gun"
      }

you = youDict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f" you chose {reverseDict[you]} \n Computer chose {reverseDict[computer]} ")

if(computer == you ):
    print("Its a draw")
else:
    if(computer == -1 and you == 0 ):
        print("you lose!")

    elif(computer == -1 and you == 1):
         print("you win!")

    elif(computer == 1 and you == -1):
         print("you lose!")


    elif(computer == 1 and you == 0):
         print("you win!")


    elif(computer == 0 and you == -1):
         print("you lose!")


    elif(computer == 0 and you == 1):
         print("you win!")

    else:
         print("something went wrong")


