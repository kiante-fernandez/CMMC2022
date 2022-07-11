# Session 1: Introduction to Python Lecture - 2022 Computational and Mathematical Modeling of Cognition
#
# Record of Revisions
#
# Date            Programmer              Descriptions of Change
# ====         ================           ======================
# 08-July-22     Michael D. Nunez              Original code

import os
import numpy as np
import pandas as pd

# Open IPython
# pwd in IPython
# ?os in IPython
# os.chdir('..')
# os.chdir('C:/Users') # For Windows, other methods are poor
# os.chdir('/home/') # For Mac ?

# Make an array
my_array = np.array([2, 3, 4])

# %paste in Python
# Talk about %paste versus CTRL+C

# What is the size of my array?
# Sometimes there are multiple ways of doing things (see Python Class discussion later today)
my_array.shape
np.shape(my_array)

# Reading errors!
# MY_array # Ask why?
# case sensitive!

# Python indexing
# Welcome to 0 indexing!
# What does each one do?
my_array[0]
my_array[1]
my_array[-1]
my_array[0:1] #this only gives you the start element:size of one
my_array[0:2] #this gives you the first two elements in the first dim
my_array[-1:]

# Printing multiple lines
print(my_array[0])
print(my_array[1])

# Approach to errors, this just happened to me
copied_array = my_array
copied_array[0] = np.nan

# Talk about Python types
print(my_array.dtype)
my_array = my_array.astype('float64')
my_array[0] = np.nan

# Python fun with new copies
copied_array = my_array
copied_array[1] = np.nan
print(copied_array)
print(my_array)

# A possibly better way
truly_copied = np.copy(my_array)
truly_copied[2] = np.nan
print(truly_copied)
print(my_array)

# Pandas data frames
#first, we create a python dic first
all_data = {"my_array": my_array, "copied_array": copied_array,
            "truly_copied": truly_copied}
my_data = pd.DataFrame(all_data)
print(my_data)
my_data
