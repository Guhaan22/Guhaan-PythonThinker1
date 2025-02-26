# Lesson 7 - For Loop (Part 2)

# ## Recap 1: Debugging Average Score Program

# ### There is a total of 3 bugs in the following program.
# ### Identify and fix the bugs:

# score_one = 80
# score_two = 90
# score_three = 75

# total = (score_one + score_two + score_three)

# average_score = total / 3

# student_name = ("Alex")

# print("Average score for" + student_name + " is: " + str("average_score"))

## Task 9: Accumulative Sum in Loop

# 1. Create a variable 'num' and assign the integer "0" to it
# 2. Create a 'for' loop that repeats 10 times
# 3. Add the sum of 'num' and the loop's parameter and print out
#    the value.
# 4. Observe what happens.
# Example:
# num = 0

# for i in range(10): 
#     num = num + i
#     print(num)
# 1st iteratio
#     num = num + i
#     print(num)

# 2nd iteration
#     num = num + i
#     print(num)

# ...

# 10th iteration
#     num = num + i
#     print(num)

# Output:
#     0
#     1
#     3
#     6
#     10
#     15
#     21
#     28
#     36
#     45
# num = num = 10
# print(num)

# ## Task 1: For Loop: 1 to 10 using range(start, stop)

# Use a 'for' loop to print numbers from 1 to 10.
# for r in range (1, 11):
#     print(r)
# ---------------------------------------------------------------

# ## Task 2: Even Numbers 2-20 Loop using
# ##         range(start, stop, step)

# Print all even numbers between 2 and 20 using a 'for' loop and
# range().
# for e in range(2, 21, 2):
#     print(e)

# ---------------------------------------------------------------

# ## Task 3: Countdown From 10 For Loop

# Use a 'for' loop and range() to count down from 10 to 1.
# for t in range(10, 0, -1):
#     print(t)

## Task 4: Word Repetition Input Loop

# Ask the user for a word and a number n. Print the word repeated
# n times (on separate lines).

# Example:
# What word would you like to repeat? <<burger>>
# How many times would you like to repeat? << 3 >>

# output:
# burger
# burger
# burger


# word = input("What word should be repeated")
# n = input("What number would you like to store")
# for w in range(int(n)):
#     print(word)

## Task 5: Personalized Greeting Loop

# Ask for a user's name and an integer n, then print a
# personalized greeting n times.

# Example:
# What is your name? <<burger>>
# How many times would you like to repeat? << 3 >>

# output:
# Nice to meet you, burger
# Nice to meet you, burger
# Nice to meet you, burger

# name = input("What name should be repeated")
# nu = input("What number would you like to store")
# for w in range(int(nu)):
#     print("Nice to meet you," +  name)

## Task 6: Sum of Five User Inputs

# Ask the user to input 5 numbers, one at a time, and print the
# sum of these numbers.

# Example:
# What is number #1 <<5>>
# What is number #2? <<2>>
# What is number #3? <<4>>
# What is number #4? <<1>>
# What is number #5? <<7>>

# output:
# Sum of the 5 numbers is 19

sum = 0
for u in range(1, 6):
    sum = sum + input("What is Number" + str(u))
    print(u)