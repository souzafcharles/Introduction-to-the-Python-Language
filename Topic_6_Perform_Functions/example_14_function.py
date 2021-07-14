# -*- coding: utf-8 -*-
"""example_14_Function.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I7NQjU7N0216xjFmgKjrAs-zrCGHuwnc
"""

# Course title: Udemy Course: Introduction to the Python Language
# Instructor: Dr. Diego Mariano
# Example adapted by: Charles Fernandes de Souza
# Date: July 14, 2021

# Function

# A function is a block of code which only runs when it is called.

def plus(a, b): # Keyword def that marks the start of the function header.
  return (a + b) # # A function can return data as a result.

sum = plus(3, 4) # You can pass data, known as parameters, into a function.
print(sum)

# In cases where you don’t know the exact number of arguments that you want to pass to a function, you can use the following syntax with *args.
def plus(*args): # The asterisk (*) is placed before the variable name that holds the values of all nonkeyword variable arguments. 
  total = 0
  for i in args:
    total += i
  return total

plus(3,4,5) # You can pass any data.