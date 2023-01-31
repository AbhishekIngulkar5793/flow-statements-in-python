"""
2. Iterative statements
-for loop
examples:
=================

s = 'Python is simple'
for i in s:
    print(i)
output is:
P
y
t
h
o
n

i
s

s
i
m
p
l
e

Process finished with exit code 0

s = 'Python is simple'
for i in s.split():
    print(i)
output is:
Python
is
simple

Process finished with exit code 0


# fetch only code form the string :4567
s = 'Python is simple use code:4567'
output = s.split(':')
print(output[-1])
output is:
4567

Process finished with exit code 0

s = 'Python is simple use code:4567'
for i in s:
    if i.isnumeric():
        print(i)
output is:
4
5
6
7

Process finished with exit code 0
================================

ht = [5,5.6,5.7,6,6.2,4.5,4.2,4,4.8]
# select candidates with ht less than 6
for num in ht:
    #print(num)
    if num < 6:
        print(num)
output is:
5
5.6
5.7
4.5
4.2
4
4.8

Process finished with exit code 0
====================================
g = [12,44,67,21,5,10,45,23,28]
# select num divisible by 5
for num in g:
    if num % 5 == 0:
        print(num)
output is:
5
10
45

Process finished with exit code 0
=====================================

g = [12,44,67,21,5,10,45,23,28]
# select num divisible by 5 and 7
for num in g:
    if (num % 5 == 0) or (num % 7 == 0):
        print(num)
output is:
21
5
10
45
28

Process finished with exit code 0
============================

g = [12,44,67,21,5,10,45,23,28]
# select num divisible by 5 and 7 and
# give me the list as an output
k =[]
for num in g:
    if (num %5 == 0) or (num %7 == 0):
        k.append(num)
    print('final list is:',k)
output is:
final list is: []
final list is: []
final list is: []
final list is: [21]
final list is: [21, 5]
final list is: [21, 5, 10]
final list is: [21, 5, 10, 45]
final list is: [21, 5, 10, 45]
final list is: [21, 5, 10, 45, 28]

Process finished with exit code 0mes = ['abhishek','pooja','anisa','ganesh','ashwini']
# fetch names starting with a
for i in nmes:
    #print(i)
    if i.startswith('a'):
        print(i)
output is:
abhishek
anisa
ashwini

Process finished with exit code 0
"""
