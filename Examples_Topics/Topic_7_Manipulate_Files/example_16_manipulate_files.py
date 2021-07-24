# -*- coding: utf-8 -*-
"""example_16_manipulate_files.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1odm1Hun_Gn0iRuK7C0Slx35y3m1IcfL_
"""
# Course title: Udemy Course: Introduction to the Python Language
# Instructor: Dr. Diego Mariano
# Example adapted by: Charles Fernandes de Souza
# Date: July 14, 2021

# Manipulate Files

# In Python, a file operation takes place in the following order:
# 1. Open a file
# 2. Read or write (perform operation)
# 3. Close the file

# Python File Write

f = open("poem2.txt", "a")
f.write(""" Surprise

The biggest
Surprise
On the library shelf
Is when you suddenly
Find yourself
Inside a book—
(The hidden you)

You wonder how
The author knew.

—Beverly McLoughland\n""")
f.close()

f = open("poem2.txt", "r")
for x in f:
  print(x)

f = open("poem3.txt", "w") # Open the file and overwrite the content:
f.write("Ops! I have deleted the content!")
f.close()

# Open and read the file after the appending:
f = open("poem3.txt", "r")
print(f.read())
