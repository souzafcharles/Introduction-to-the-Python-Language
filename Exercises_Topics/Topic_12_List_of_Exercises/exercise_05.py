# -*- coding: utf-8 -*-
"""Exercise_05.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14pp3boahk2F-ZYrfyOqUXzd_2unZly3T
"""

# Course title: Udemy Course - Introduction to the Python Language
# Instructor: Dr. Diego Mariano
# Example adapted by: Charles Fernandes de Souza
# Date: July 18, 2021

# Resolution of Exercise 05

number_01 = int(input("Enter the first number: "))
sign = input("Enter the Sign (mathematics): ")
number_02 = int(input("Enter the second number: "))
 
if sign == "+":
     result = number_01 + number_02
 
elif sign == "-":
     result= number_01 - number_02
 
elif sign == "/":
     result = number_01 / number_02
 
elif sign == "*":
     result = number_01 * number_02
 
else:
     print("Invalid signal.")
 
print(result)