import random
import math
lower = int(input("enter lower bond: " ))
upper = int(input("enter upper bond: " ))
x= random.randint(lower, upper)
total_chances= math.ceil(math.log(upper - lower + 1, 2))
print("\n\tyou've ",total_chances," chances to guess the integer!\n")
count = 0
flag = False
while count < total_chances:
    count += 1
    guess = int(input("guess a number: "))
    if x==guess:
        print("congratulation you did it ", count, " try")
        flag = True
        break
    elif x > guess:
        print("you guessed too low!")
    elif x < guess:
        print("you guessed too high!")
if not flag:
    print("\nThe number is %d" % x)
    print("\tBetter luck next time!")