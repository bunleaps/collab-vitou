# Idea: Rock, Paper, Scissor

# Import Modules
import random

rock = 0
paper = 1
scissor = 2

iput = input(
"""
Rock, Paper, Scissor
====================
 0) Rock
 1) Paper
 2) Scissor
====================
Pick: """
)
answer = int(iput)

computer = random.randint(0, 2)

# Rock
if answer == rock and computer == 2:
    
    print("Win - User: Rock | Computer: Scissor")
    answer
elif answer == rock and computer == 1:
    print("Lose - User: Rock | Computer: Paper")
    answer
elif answer == rock and computer == 0:
    print("Tie - User: Rock | Computer: Rock")

# Paper
if answer == paper and computer == 2:
    
    print("Lose - User: Paper | Computer: Scissor")
elif answer == paper and computer == 1:
    
    print("Tie - User: Paper | Computer: Paper")
elif answer == paper and computer == 0:
    
    print("Win - User: Paper | Computer: Rock")

# Scissor
if answer == scissor and computer == 2:
    
    print("Tie - User: Scissor | Computer: Scissor")
elif answer == scissor and computer == 1:
    
    print("Win - User: Scissor | Computer: Paper")
elif answer == scissor and computer == 0:
    
    print("Lose - User: Scissor | Computer: Rock")


