"""
how to debug a code?
---------------------------------

category = input('Enter category:')
if category == 'mobile':
    sub_cat = input('Enter sub categories:')
    if sub_cat == 'smart phones':
        print('List of smart phones\nmi\nrealme\napple\noppo\nvivo\noneplus\nsamsung\npoco')
        brand = input('select the brand for your mobile:')
        if brand == 'mi':
            ram = int(input('Enter RAM size:'))
            if ram == 8:
                print('price is rs',21000)
            elif ram == 12:
                print('Price is rs',30000)
                if brand == 'realme':
                    print('out of stock')
                    if brand == 'apple':
                        version = int(input('which iphone you want?:'))
                        if version == 'iphone 11':
                            print('Price is rs',50000)
                            if version == 'iphone 12':
                                print('Price is rs',65000)
                                if version == 'iphone 13':
                                    print('Price is rs',80000)
                                else:
                                    print('we don/t have that phone')
else:
    print('select appropriate type please')
=======================================

num = -1
if num > 0:
    print('Number is positive')
else:
    print('number is -ve')

# 2. Iterative statement:
# from a collection of elements we retrieve one element at a time
[10,20,30]
one after another will fetch one element at a time
10
20
30
-for loop
syntax:
for variable_name in sequence/iterable:

#example
k = [10,20,30,40,50]
for value in k:
    print(value)
output is:
10
20
30
40
50
==============================================

a = ['abhi','shreyal','asha',1,23.55]
for nm in a:
    print(nm)
output is:
abhi
shreyal
asha
1
23.55
# Iterables : collections
#string
#list
#tuple
#set
#dictionary
#frozenset
#bytes
#bytearray
#range
================================

for num in range(0,101):
    print(num)
=================================
# print 1- 100 odd numbers using for loop
-----------------------------
use # print(list(range(1,101,2)))

for i in range(2,101,2):
    print(i,end=' ')
output is:

2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100
Process finished with exit code 0
==============================================
google : python exercises on geeksforgeeks
========================================
python exercises,practice,challenges - PYnative
https://pynative.com/python-exercises-with-solutions
=================================
Python Exercises, Practice, Solution - w3resource
https://w3resource.com/python-exercises
============================

text = 'maam'
if text == text[::-1]:
    print('text, is palindrome')
else:
    print('its not palindrome')
output is:
text, is palindrome




Process finished with exit code 0
ps-



"""



