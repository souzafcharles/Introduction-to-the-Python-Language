# -*- coding: utf-8 -*-
"""Exercise_03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AMdduWECZ0MYHyKcA56ypEGai6Rvm7hN
"""

# Course title: Udemy Course - Introduction to the Python Language
# Instructor: Dr. Diego Mariano
# Example adapted by: Charles Fernandes de Souza
# Date: July 18, 2021

# Resolution of Exercise 03

from math import sqrt
a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))
c = int(input("Enter the value of C: "))
 
delta = b**2 -4*a*c
delta_root = sqrt(delta)
 
if delta_root < 0:
     print("Negative Delta")
else:
     x1 = (-b + delta_root)/2*a
     x2 = (-b + delta_root)/2*a
 
     print("The roots are", x1, "and", x2)