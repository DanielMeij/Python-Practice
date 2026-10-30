import random
#1. 
print("-1-")
Input = input("Type in a String: ")
print(Input.upper())

#2
print("-2-")
number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
print(f"Number 1: {number1}")
print(f"Number 2: {number2}")
total1 = number1 + number2
print(f"{number1} + {number2} = {total1}")

#3
print("-3-")
answer1 = "yes"
number3 = int(input("Enter a Number: "))
total2 = number3
print(f"total: {total2}")
while answer1 == "yes":
    number4 = int(input("Enter a Number: "))
    total2 = total2 + number4
    print(f"total: {total2}")
    answer1 = input("Do you want to play again? yes/no; ")
    if answer1 not in ["yes", "no"]:
        answer1 = "yes"
        print("Error: must be yes or no.")


#4
print("-4-")
answer2 = "yes"
while answer2 == "yes":
    number5 = int(input("Enter a number: "))
    number6 = int(input("Enter a number: "))
    final = random.randint(number5, number6)
    print(f"Final Number: {final}")
    answer2 = input("Do you want to play again? yes/no: ")
    if answer2 not in ["yes", "no"]:
        answer2 = "yes"
        print("Error: must be yes or no.")

print("-5-")
right = 0
left = 0
for i in range(10):
    number7 = random.randint(1, 100)

    if number7 % 2 == 0:
        print("RIGHT")
        right = right + 1
    else:
        print("LEFT")
        left = left + 1
print(f"Left: {left}")
print(f"Right: {right}")
