# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
print("Welcome to my computer quiz")

playing = input("Do you want to play?")

if playing !="yes":
    quit()

print("Okay! Let's play! :")
score = 0

answer = input("Is the coding language Python, named after a snake? ")
if answer == "no":
    print('correct!!')
    score += 1
else:
    print('Incorrect!!!')

answer = input("What does CPU stand for?")
if answer =="central processing unit":
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!!')

answer = input("What does RAM stand for?")
if answer =="random access memory":
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!!')

answer = input("What does HTML stand for?")
if answer =="hypertext markup language":
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!!')

answer = input("What does PDF stand for?")
if answer =="portable document format":
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!!')

answer = input("What does PNG in computer image format stand for?")
if answer =="portable network graphics":
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!!')


answer = input("What does GB in computer stand for?")
if answer =="giga bytes":
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!!')


answer = input("What does CD in computer stand for?")
if answer =="compact disk":
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!!')


answer = input("What does DVD stand for?")
if answer =="digital video disk":
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!!')


answer = input("What does KB stand for?")
if answer =="kilo bytes":
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!!')


print("You got " + str(score) + " questoins correct!")
print("You got " + str((score/10) *100) + "%. ")