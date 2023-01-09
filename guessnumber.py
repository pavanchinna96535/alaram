import random
num=random.randrange(1,10)
print(num)
guess_num=int(input("enter the number: "))

while (guess_num!=num):
    if (guess_num>num):
        print("entered number is bigger ")
        num=random.randrange(1,10)
        print(num)
        guess_num=int(input("enter the number: "))
    elif(guess_num<num):
         print("entered number is smaller ")
         num=random.randrange(1,10)
         print(num)
         guess_num=int(input("enter the number: "))
    else:
        break

print("You won the game")
print("would you like to try again!!")

