# Lesson 8 - Importing Libraries, Boolean & Conditions

## Recap 1: Product of 5 numbers

# Write a program to calculate the product (multiplication) of 5
# numbers.

# 1. Using a for loop, ask the user for 5 numbers one at a time.
# 2. Calculate the multiplication for these 5 numbers and print
#    it out.
# t = 1
# for y in range(5):
#    ger = input("what is number" + t)
#    t = t + 1   

## Task 1: 'time' library

# **Task 1a**:
# Import the 'time' library and make use of the 'time.sleep()'
# function to create a 10 seconds countdown timer that counts
# to 1, printing the number of seconds remaining every second.

# **Task 1b**:
# Modify your code from Task 1a to include an 'input()' function
# asking the user for the number to countdown from, before
# counting down every second from the number given by the user.me
# import time

# range(stop)
# range(start, stop) => step is 1
# range(start, stop, step)
# for i in range(3060, 0, -1):
#    print(i)
#    time.sleep(1)

## Task 2: 'random' library

# **Task 2a**:
# Import the 'random' library and create a program that randomly
# output a number between 1 to 6
# import random
# random.randint(1, 6)
# print(random.randint)


# **Task 2b**:
# Using the 'random' library, create 20 numbers between 0 and
# 9999 randomly.

## Task 3: Print Boolean Value & Condition

# **Task 3a**:
# Assign a boolean value to a variable and print it.
# eurt = True
# print(str(eurt))

# **Task 3b**:
# Create 2 variables both holding the "True" boolean.
# Print out the result of comparing the 2 variables using
# the "==" operator.
# tryu = True
# uiopp = True
# print(tryu == uiopp)

# **Task 3c**:
# Now, assign 1 variable the "True" boolean, and assign another
# variable the "False" boolean.


# Print out the result of comparing the 2 variables using
# the "==" operator.
# trew = True


## Task 4:

# **Task 4a**: Math Question Generator
# Using the 'random' library, generate 2 numbers between 1 and 50
# that the user must add together.

# The output should be one of the following:
# 1. True (If the answer is correct)
# 2. False (If the answer is wrong)

# Example:
# What is 2 + 5? << 7 >>
# True
# import random
# num1 = random.randint(1, 50)
# num2 = random.randint(1, 50)
# user_ans = input("What is " + str(num1)+ "+" + str(num2))
# ans = num1 + num2
# print(int(user_ans)== ans)

# **Task 4b**: Range Guesser
# Create a program that generates a random number between 1 and
# 50.

# The user should input a range (two numbers: start and end).

# The program checks if the random number falls within the user's
# range.

# The output should be one of the following:
# 1. True (If the answer is correct)
# 2. False (If the answer is wrong)

import random
random.randint(1, 50)
num1 = input("what variable should start be")
n