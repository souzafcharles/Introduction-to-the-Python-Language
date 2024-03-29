# -*- coding: utf-8 -*-
"""example_19_Dictionaries.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KuFfOgmpUA8k2VAjpbre3aqZTVvV8PR1
"""
# Course title: Udemy Course: Introduction to the Python Language
# Instructor: Dr. Diego Mariano
# Example adapted by: Charles Fernandes de Souza
# Date: July 18, 2021

# Dictionaries are used to store data values in key:value pairs.

thisDictionary = {
  "brand": "Volkswagen",
  "model": "Fusca",
  "year": "1938"
}
print(thisDictionary)

# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

print(thisDictionary["model"]) # Print the "model" value of the dictionary. 

# Inside the for loop, on every iteration, you print out the dictionary value:
for key in thisDictionary:
  print(key+":"+thisDictionary[key])

# Inside the for loop, on every iteration, you print out the dictionary in tuple:
for index in thisDictionary.items():
  print(index)

# The values in dictionary items can be of any data type:
thisDictionary = {
  "brand": "Volkswagen",
  "model": "Fusca",
  "electric": False,
  "year": 1938,
  "colors": ["red", "white", "blue"]
}
print(thisDictionary)
