import math
import numpy as np
import random
import urllib.request
from functools import reduce, partial

fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])

def isFibonacci(number):
   source = fib_series(30)
   isFibonacciLambda = lambda x: True if x in source else False
   return isFibonacciLambda(number)

def filterFibonacciInList(l):
    source = fib_series(30)
    return list(filter(lambda x: True if x in source else False,l))

def addEvenOdd(l1,l2):
    return [a+b for a,b in zip(filter(lambda x: x%2 == 0, l1), filter(lambda x: x%2 == 1, l2))]

def removeVowel(str):
    return ''.join([x for x in str if x.lower() not in {'a','e','i','o','u'}])

def sigmoid(weights):
    return [round(1 / (1 + math.exp(-x)),2) for x in weights]

def shiftEncoder(str):
    if(not str.isalpha()):
        raise ValueError("Only alphabets allowed")
    if(not str.islower()):
        raise ValueError("Only lower case allowed") 
    return "".join([chr(int((ord(i) + 5 - 97)%26 )+97) for i in str])

def findBadWords(paragraph,url):
    return [x for x in paragraph.lower().split() if x in [line.decode("utf-8").replace("\n","") for line in urllib.request.urlopen(url)]]

def addEvenNumbers(l):    
    return reduce(lambda a,b:a+b,[x for x in l if x%2==0])

def findBiggestCharacter(str):
    return reduce(lambda a,b:a if ord(a)>ord(b) else b,str.lower())

def addThirdNumber(l):
    return reduce(lambda a,b: a+b,l[2::3])

def generateNumberPlates(limit):
    return(['KA'+str(random.randint(10,99))+chr(random.randint(65,90))+chr(random.randint(65,90))+str(random.randint(1000,9999)) for x in range(limit)])

def generateNumberPlatesOption(stateCode, start = 1000, end = 9999, limit = 15):
    return ([stateCode.upper()+str(random.randint(10, 99))+chr(random.randint(65,90))+chr(random.randint(65,90))+str(random.randint(start,end)) for x in range(limit)])

generateNumberPlatesPartial = partial(generateNumberPlatesOption,start = 2222,end = 3333)

