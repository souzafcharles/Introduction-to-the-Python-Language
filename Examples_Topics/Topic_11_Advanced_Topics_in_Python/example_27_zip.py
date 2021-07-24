# -*- coding: utf-8 -*-
"""example_27_Zip.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12M-wAj1zFhmvTVA_pmha7_S9a12OlFbn
"""
# Course title: Udemy Course - Introduction to the Python Language
# Instructor: Dr. Diego Mariano
# Example adapted by: Charles Fernandes de Souza
# Date: July 18, 2021

# Filter() Function

animals_A = ("Albatross", "Coyote", "Orangutan")
animals_B = ("Alligator", "Chameleon", "Ostrich")

animals_list = zip(animals_A, animals_B)

# The tuple() function to display a readable version of the result:
print(tuple(animals_list))


animals_C = ["Albatross", "Coyote", "Orangutan"]
animals_D = ["Alligator", "Chameleon", "Ostrich"]
status = ["very wild", "very wild", "litle wild"]

for name_C, name_D, statusWild in zip(animals_C, animals_D, status):
  print(name_C +" and "+name_D +" are "+ statusWild)
