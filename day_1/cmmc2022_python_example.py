# Python Script Example: 2022 Computational and Mathematical Modeling of Cognition
#
# Record of Revisions
#
# Date            Programmer              Descriptions of Change
# ====         ================           ======================
# 09-July-22        Michael Nunez               Original code

import os
import numpy as np
import pandas as pd

# Q1.0
# This is the answer the the example problem Q1.0 in a comment
this_variable = 1
print(this_variable)

# Out[3]: 1

# Q1.1
#you needed to import numpy (as shown above)
my_numpy_array = np.array([5, 6, 1])

# Q1.2
another_array = np.zeros((2,4,6))
#create 2 matrix that are 4 by 6

another_array.ndim #3 dimensions
another_array.shape #3 dimensions
print(another_array)

another_array[0,0,0] # return 1st element
another_array[0,3,0] # return 4th element 2nd dimension

another_array[0,0,-1] #? return last element of 3rd dimension
#the trick is to use negative. Not sure though

another_array[0,3,-1] #is what he wanted

# Q1.3
another_array = np.zeros((2, 4, 6))
new_array = another_array
new_array[1, 2, 2] = 1
print(another_array[1, 2, 2])

#it modfied the other array they are referencing the same thing in the enviroment
another_array = np.zeros((2, 4, 6))
new_array = np.copy(another_array)
new_array[1, 2, 2] = 1
print(another_array[1, 2, 2])

# Q1.4
#> magic functions will not work in the python script
#> you need to you these in the ipython terminal

# Q1.5
#> cd
#> pwd
#> !ls
#> 

# Q1.6
#> pip install in terminal no? While in your conda enviroment

#Q 1.7
sample_scores = np.array([1, 6, 7, 8, 9, np.nan])
print(np.mean(sample_scores))
#becasue we have an na
#we could subset to remove it
print(np.mean(sample_scores[0:-2]))
#you can use nanmean to solve this problem
print(np.nanmean(sample_scores))

#Q 1.8
res_array = np.array(range(1, 17))**2
res_array = np.array(np.arange(1, 17))**2

res_array = np.reshape(res_array, [2,2,2,2])
res_array.ndim
res_array.shape

#Q 1.9
#load files
InsectSprays_df = pd.read_csv("~/Documents/OSU/summer_schools/CMMC2022/data/InsectSprays.csv")

InsectSprays_dic = InsectSprays_df.to_dict()
print(InsectSprays_dic.keys())
print(InsectSprays_dic.values())

#Q 1.10
np.random.seed(1234) # Set the random seed
speed_sec = np.zeros(10)
sim_speed = np.random.uniform(size=5) # Speed simulation in seconds
speed_sec[::2] = sim_speed * 10
speed_sec[1::2] = sim_speed
print(sim_speed)

code_type = []

for i in range(1,6):
    code_type.append("forloop{fnum}".format(fnum =  i))
    
    
Dictionary_res = {'language': ['R','Python'] * sim_speed.shape[0], 'code_type':code_type, 'speed_sec': speed_sec}

TEST = pd.DataFrame.from_dict(Dictionary_res, orient='index')
TEST = TEST.transpose()

#we could also you the repeat

#Q 1.11
Dictionary_res = {'year': , 'people': ["Roman"], 'government': ['republic', 'empire']]}


##################################################

import numpy as np
from time import time
two_dice = np.random.choice(np.arange(1,7), 2, replace = True)

def score_game(two_dice):
    if (sum(two_dice) % == 0:
      score = sum(two_dice) * np.min(two_dice)
      print(score)
    else:
      score = -3 * sum(two_dice)
      print(score)



score_game(two_dice)

#Q.2.2

double_plus = np.array([])

for i in range(3, 18, 2):
  double_plus = np.append(double_plus,np.array([i]), axis=0)


#Q.2.3

grass = "green"
def color_it(color_me, grass_me):
    global grass #make it know we want the global
    grass_me = grass
    color_me = "blue"
    grass = "blue"
    colorful_items = np.array([(color_me, grass_me)])
    return colorful_items



sky = "grey"
ground = "brown"
these_items = color_it(sky, ground)
print(these_items)

#Q.2.4

class MyClass:
    """A simple example class"""
    classnum = 12345
    def famous(self):
      return 'hello world'


new_stuff = MyClass()
new_stuff.classnum
new_stuff.famous()


#>python class creates an object that we can do things with.
#>it is a way to group functions can will be used together
import cmath

# Complex number class
class ComplexNum:
    """Creates a complex number"""
    numtype = 'complex'
    def __init__(self, realpart, imagpart):
      self.r = realpart
      self.i = imagpart
      self.im = imagpart.imag
    def vec_length(self):
      return np.sqrt(self.r**2 + self.i**2)
    def phase_angle(self):
#      return (cmath.phase(self.r + self.i *1j))
      return np.angle(self.r + self.i *1j, deg = True)


my_num = ComplexNum(3.0, 4.0)
print(my_num)
print((my_num.r, my_num.i))
print(my_num.numtype)
print(my_num.vec_length())
print(my_num.phase_angle())

my_num = ComplexNum(-4.0, -3.0)
print(my_num.phase_angle())

##Q.2.5, Q.2.6, 2.7 (see sequences.py)


def fibonacci(n):
    """
    Generates the Fibonacci sequence. This is where each number is the sum 
    of the two preceding ones
    Parameters
    ----------
    n: the length of the sequence to generate
    Returns
    _________
    an np.array of the corresponding n fibonacci elements
    """
    result = np.array([0, 1])
    temp_n = 2
    while temp_n < n:
      result = np.append(result, result[temp_n - 1] + result[temp_n - 2])
      temp_n += 1
    return (result)


# 2.8
# import requests
# 
# try:
#     url = "https://tinyurl.com/pipsTitanic"
#     r = requests.get(url)
#     print("HTML:\n", r.text)
# except:
#     print("Invalid URL or some error occured while making the GET request to the specified URL")

#OR
url = "https://tinyurl.com/pipsTitanic"

pipsTitanic=pd.read_csv(url)

for i in range(1, len(pipsTitanic)):
    if (pipsTitanic["Sex"][i - 1] == 'female') & (pipsTitanic["Sex"][i] == 'male'):
      print(str(i)," I'll never let go, Jack. I'll never let go. I promise")


# 2.9

def counting(start_num = 1):
  if start_num > 0:
    while (start_num < 100):
      start_num += 0.1
      print(start_num)
  else start_num < 0:
    print("I'm not good at counting backwards")
    while (start_num > -100):
      start_num -= 1
      print(start_num)


start_num = 1
if start_num > 0:
    while (start_num < 100):
      print(start_num)
      start_num += 0.1
    break
else start_num < 0:
    print("I'm not good at counting backwards")
    while (start_num > -100):
      start_num -= 1
      print(start_num)
   break



