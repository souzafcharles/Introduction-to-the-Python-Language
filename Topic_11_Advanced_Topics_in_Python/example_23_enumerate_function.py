# -*- coding: utf-8 -*-
"""example_23_Enumerate_Function.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FuomkvrOSdr3W56HB4IINhUaDD-VraMT
"""

# Course title: Udemy Course - Introduction to the Python Language
# Instructor: Dr. Diego Mariano
# Example adapted by: Charles Fernandes de Souza
# Date: July 18, 2021

# Enumerate() Function

# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate object.

# Convert a tuple into an enumerate object:
animalsList = ('elephant', 'giraffe', 'moose', "penguin", "squirrel")
enumerateFunction = enumerate(animalsList)
print(list(enumerateFunction))

# Enumerate a list of items:
animalsList = ('elephant', 'giraffe', 'moose', "penguin", "squirrel")
for i, animal in enumerate(animalsList):
  print (i, animal)