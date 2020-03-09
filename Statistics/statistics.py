# To calculate Mean, Median and Mode with Python without using external libraries.
# 1. Mean (to get the average of a list)
n = int(input("Enter N :"))
lst = []
for i in range(0,n):
    ele = int(input("Enter element :"))
    lst.append(ele)
l = len(lst)
mean = sum(lst)/l
print("Mean :")
print(mean)

# 2. Median
# List of elements to calculate median : The median is the middle number in a group of numbers.
# This code calculates Median of a list containing numbers
n_num = [1, 2, 3, 4, 5] 
n = len(n_num) 
n_num.sort() 

if n % 2 == 0: 
    median1 = n_num[n//2] 
    median2 = n_num[n//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = n_num[n//2] 
print("Median is: " + str(median)) 

"""
On python 3.x:

>>> 1/2
0.5
>>> 1//2
0
>>> 1.0//2
0.0

so // operator always carries out floor division,
it always truncates the fraction and moves to the left of the number line.
"""

# Mode : The mode is the number that occurs most often
# within a set of numbers. This code calculates Mode of a list containing numbers:

from collections import Counter 

# list of elements to calculate mode 
n_num = [1, 2, 3, 4, 5, 5] 
n = len(n_num) 

data = Counter(n_num) 
get_mode = dict(data) 
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 

if len(mode) == n: 
    get_mode = "No mode found"
else: 
    get_mode = "Mode is / are: " + ', '.join(map(str, mode)) 
    
print(get_mode) 

"""
We will import Counter from collections library which is a built-in module in Python 2 and 3.
This module will help us count duplicate elements in a list.
We define a list of numbers and calculate the length of the list.
We then call Counter (a dict subclass) which helps to count hashable objects,
and we then convert it to dict object. We then initialize a list with a
For Loop to compare all the dict values (Number of elements) to the max
of all dict values (count of most occurring element) and it returns all the elements equal to max count.
If the elements returned are
equal to the number of total elements in a list then we print out ‘No mode’, else we print out the modes returned.
"""