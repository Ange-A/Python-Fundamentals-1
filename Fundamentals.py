library(reticulate)

import pandas as pd
import numpy as np


the_world_is_flat =  True
if the_world_is_flat:
  print("Be careful not to fall off")



print("""\
    Usage: thingy [OPTIONS]
    -H           Display this usage message
    -h hostname  Hostname to connect to
    """)


print('Py' 'thon')


word = "Python"
print(word)

word[0]

word[5]


word[-1]

word[-2]

word[-6]


'j' + word[1:]
'py'+word [:2]
#Fibonnaci Series

#sum of two elemenst defines the next


a, b = 0, 1
while a < 10:
  print(a)
a, b = b, a+b


a, b = 0, 1
while a < 1000:
  print(a)
a,b = b, a+b


#if statements

x = int(input("Please enter an integer: "))
if x < 0:
  x = 0
print('Negative change to Zero')
elif x == 0:
  print('Zero')
elif x == 1:
  print('Single')
else:
  print('More')


x = int(input("Please enter an integer: "))
if x < 0:
  x = 0
print('Negative')
elif x == 0:
  print('singe')
elif x == 1:
  print('one')
else:
  print('More')


#for statements


words = ['cat', 'window', 'defenesreate']
for w in words:
  print(w, len(w))


for i in range(0, 10, 3):
  print(i)


a= ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
  print(i, a[i])

list(range(5))


#prime_numbers

for n in range(2, 10):
  for x in range(2, n):
  if n % x == 0:
  print(n, 'equals', x, '*', n//x)
break

else:
  print(n, 'is a prime number')


# even numbers


for num in range(2, 10):
  if num % 2 == 0:
  print("Found an even number", num)
continue
print("Found a number", num)


# Defining Functions(Fibonacci):


def fib(n):
  
  a, b = 0, 1
while a < n:
  print(a, end= " ")
a, b = b, a+b
print()

fib(500)



def fib2(n):
  result = []
a, b = 0, 1
while a < n :
  result.append(a)
a, b = b, a+b
return result


def fib2(n):
  result = []
a, b = 0, 1
while a < n:
  result.append(a)
a, b = b, a+b
return result


f100 = fib2(100)
f100



#default Argument Values


def ask_ok(prompt, retries= 4, reminder = 'Please Try again!'):
  while TRUE:
  ok = input(prompt)
if ok in ('y', 'ye', 'yes'):
  return True
if ok in ('n','no','nop','nope'):
  return False
retries = retries -1
if retries < 0:
  raise ValueError('invalid response')
print(reminder)



i = 5

def f(arg = i):
  print(arg)

i = 6
f()
