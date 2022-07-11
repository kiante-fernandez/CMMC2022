# Session 2: Flow Control Lecture - 2022 Computational and Mathematical Modeling of Cognition
#
# Record of Revisions
#
# Date            Programmer              Descriptions of Change
# ====         ================           ======================
# 09-July-22     Michael D. Nunez              Original code

import os
import numpy as np
import warnings

# IF Statements
age1 = 50
age2 = 50
if age1 == age2:
    print("even")  # Notice the spacing
    
# Notice the extra line above

age1 = 50
age2 = 52
if age1 < age2:
    print("older")  

# Note what doesn't work with spacing
age1 = 50
age2 = 52
if age1 < age2:
print("older")  

# Note what doesn't work with spacing
age1 = 50
age2 = 52
if age1 > age2:
    mean_age = np.mean(np.array((age1, age2)))  # Note the number of necessary parentheses ()
    print('younger') # This is not part of the if statement and always prints

# Note how NOT use "bang" statement
age1 = 50
age2 = 52
if !(age1 > age2):  # This doesn't work
    mean_age = np.mean(np.array((age1, age2)))
    print('younger') 


# Note how to use "not"
age1 = 50
age2 = 52
if not (age1 > age2):  # This works
    mean_age = np.mean(np.array((age1, age2)))
    print('older')


if ~(age1 > age2):  # This works
    mean_age = np.mean(np.array((age1, age2)))
    print('older')


# Note how to use "and" and "&"
age1 = 50
age2 = 52
age3 = 55
if (age3 > age2) and (age3 > age1):  # This works
    print('oldest')
    
if (age3 > age2) & (age3 > age1):  # This works
    print('oldest')

# Note how to use "or" and "|"
age1 = 50
age2 = 102
age3 = 55
if (age3 > age2) | (age3 > age1):  # This works. note it is style to use ()
    print('older')

# Note how to use "or" and "|"
age1 = 50
age2 = 102
age3 = 55
if (age3 > age2) or (age3 > age1):  # This works
    print('older')


# If, elif, else
age1 = 50
age2 = 40
age3 = 30
if age1 > age2:
    print('older than second')
elif age1 > age3:
    print('older than third')
else:
    print('not older')

# Compared to vectorized ifelse() in R
vec1 = np.array([1, 2.4, np.nan, np.pi])
close_pi = np.where(np.round(vec1, decimals=2) == 3.14, "is_pi", "not_pi")
print(close_pi)

# While loops
np.random.seed(2022)  # Why does the following code produce the same values every time?
wallet = 10
while wallet > 0:
    throws = np.random.choice([1, 2, 3, 4, 5, 6], 3, replace=True)  # Roll 3 dice
    if len(set(throws)) == len(throws):  # If 3 different values
        wallet += 1
        break  # Note that this breaks out of the while loop
    else:
        wallet -= 3
    print(wallet)
print("Final Euros:", wallet)

# For loops
# We can play three times
for i in range(10):  # Play ten rounds
    # What will i be on the first iteration?
    if len(set(throws)) == len(throws):  # If 3 different values
        wallet += 1
        break  # Note that this breaks out of the while loop
    else:
        wallet -= 3
    print(wallet)
print("Final Euros:", wallet)

# You can also index over elements
vec1 = np.array([1, 2.4, np.nan, np.pi])
for element in vec1:
    if np.round(element, decimals=2) == 3.14:
        print('Pi!')
    else:
        print('Not Pi enough!')


# Definitions (Functions in R):
def hello_you(name='Michael'):
    """This function prints Hello and then the input"""
    print('Hello %s' % name)


# ^ Definitions are two spaces above the next line
hello_you()
hello_you('Crash the dog')

# An example of a definition I actually use:
def simulratcliff(Nu=1, Alpha=1, Tau=.4, Beta=.5,  Varsigma=1, rangeTau=0, rangeBeta=0, Eta=0):
    """
    SIMULRATCLIFF  Generates data according to a drift diffusion model with optional trial-to-trial variability


    Reference:
    Tuerlinckx, F., Maris, E.,
    Ratcliff, R., & De Boeck, P. (2001). A comparison of four methods for
    simulating the diffusion process. Behavior Research Methods,
    Instruments, & Computers, 33, 443-456.

    Parameters
    ----------
    N: a integer denoting the size of the output vector
    (defaults to 100 experimental trials)

    Alpha: the mean boundary separation across trials  in evidence units
    (defaults to 1 evidence unit)

    Tau: the mean non-decision time across trials in seconds
    (defaults to .4 seconds)

    Nu: the mean drift rate across trials in evidence units per second
    (defaults to 1 evidence units per second, restricted to -5 to 5 units)

    Beta: the initial bias in the evidence process for choice A as a proportion of boundary Alpha
    (defaults to .5 or 50% of total evidence units given by Alpha)

    rangeTau: Non-decision time across trials is generated from a uniform
    distribution of Tau - rangeTau/2 to  Tau + rangeTau/2 across trials
    (defaults to 0 seconds)

    rangeZeta: Bias across trials is generated from a uniform distribution
    of Zeta - rangeZeta/2 to Zeta + rangeZeta/2 across trials
    (defaults to 0 evidence units)

    Eta: Standard deviation of the drift rate across trials
    (defaults to 3 evidence units per second, restricted to less than 3 evidence units)

    Varsigma: The diffusion coefficient, the standard deviation of the
    evidence accumulation process within one trial. It is recommended that
    this parameter be kept fixed unless you have reason to explore this parameter
    (defaults to 1 evidence unit per second)

    Returns
    -------
    Numpy complex vector with  reaction times (in seconds) multiplied by the response vector
    such that negative reaction times encode response B and positive reaction times
    encode response A

    Also returns single-trial drift rates


    Converted from simuldiff.m MATLAB script by Joachim Vandekerckhove
    See also http://ppw.kuleuven.be/okp/dmatoolbox.
    """

    if (Nu < -5) or (Nu > 5):
        Nu = np.sign(Nu) * 5
        # warnings.warn('Nu is not in the range [-5 5], bounding drift rate to %.1f...' % (Nu))

    if (Eta > 3):
        # warning.warn('Standard deviation of drift rate is out of bounds, bounding drift rate to 3')
        eta = 3

    if (Eta == 0):
        Eta = 1e-16

    # Called sigma in 2001 paper
    D = np.power(Varsigma, 2) / 2

    # Program specifications
    eps = 2.220446049250313e-16  # precision from 1.0 to next double-precision number
    delta = eps

    r1 = np.random.normal()
    mu = Nu + r1 * Eta
    bb = Beta - rangeBeta / 2 + rangeBeta * np.random.uniform(0,1)  #Numba likes np.random.uniform(0,1) not ()
    zz = bb * Alpha
    finish = 0
    totaltime = 0
    startpos = 0
    Aupper = Alpha - zz
    Alower = -zz
    radius = np.min(np.array([np.abs(Aupper), np.abs(Alower)]))
    while (finish == 0):
        lambda_ = 0.25 * np.power(mu, 2) / D + 0.25 * D * np.power(np.pi, 2) / np.power(radius, 2)
        # eq. formula (13) in 2001 paper with D = sigma^2/2 and radius = Alpha/2
        F = D * np.pi / (radius * mu)
        F = np.power(F, 2) / (1 + np.power(F, 2))
        # formula p447 in 2001 paper
        prob = np.exp(radius * mu / D)
        prob = prob / (1 + prob)
        dir_ = 2 * (np.random.uniform(0,1) < prob) - 1
        l = -1
        s2 = 0
        while (s2 > l):
            s2 = np.random.uniform(0,1)
            s1 = np.random.uniform(0,1)
            tnew = 0
            told = 0
            uu = 0
            while (np.abs(tnew - told) > eps) or (uu == 0):
                told = tnew
                uu = uu + 1
                tnew = told + (2 * uu + 1) * np.power(-1, uu) * np.power(s1, (F * np.power(2 * uu + 1, 2)))
                # infinite sum in formula (16) in BRMIC,2001
            l = 1 + np.power(s1, (-F)) * tnew
        # rest of formula (16)
        t = np.abs(np.log(s1)) / lambda_
        # is the negative of t* in (14) in BRMIC,2001
        totaltime = totaltime + t
        dir_ = startpos + dir_ * radius
        ndt = Tau - rangeTau / 2 + rangeTau * np.random.uniform(0,1)
        if ((dir_ + delta) > Aupper):
            T = ndt + totaltime
            XX = 1
            finish = 1
        elif ((dir_ - delta) < Alower):
            T = ndt + totaltime
            XX = -1
            finish = 1
        else:
            startpos = dir_
            radius = np.min(np.abs(np.array([Aupper, Alower]) - startpos))

    result = T * XX
    return result


# Global versus local variables (this works differently to R):
sweet_name = 'Crash'
def hello_you2(name='Michael'):
    """This function prints Hello and then the input"""
    sweet_name = name + 'y'  # Note how Python can concatenate strings
    print('Hello %s' % name)
    return sweet_name  # Notice the "return"


the_name = hello_you2("Joachim")
print(the_name)
print(sweet_name)


# Global versus local variables (this works differently to R):
sweet_name = 'Crash'
def hello_you3(name='Michael'):
    """This function prints Hello and then the input"""
    print('Hello %s' % name)
    return sweet_name  # Notice the "return"

the_name = hello_you3("Joachim")
print(the_name)
print(sweet_name)

# Raise an error
def hello_you4(name='Michael'):
    """This function prints Hello and then the input"""
    if name == "world":
        # raise ValueError('This is a cliché')
        warnings.warn('This is a cliché')
    print('Hello %s' % name)

hello_you4("world")


# An example of Python classes
class MyClass:
    """A simple example class"""
    classnum = 12345
    def famous(self):
        return 'hello world'



new_stuff = MyClass()
new_stuff.classnum
new_stuff.famous()


