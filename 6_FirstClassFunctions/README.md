
PART 2

Assignment 2 (500)
1. Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not. You can use a pre-calculated list/dict to store fab numbers till 10000 
2. Using list comprehension (and zip/lambda/etc if required) write expressions that:
   1. add 2 iterables a and b such that a is even and b is odd
   2. strips every vowel from a string provided (tsai>>t s)
   3. acts like a sigmoid function for a 1D array
   4. takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
3. A list comprehension expression that takes a ~200-word paragraph, and checks whether it has any of the swear words 
4. Using reduce function:
   1. add only even numbers in a list
   2. find the biggest character in a string (printable ASCII characters)
   3. adds every 3rd number in a list
5. Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999 
6. Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided


## Solution


|Q|         Function          |                 Implementation                                |
|-| :----------------------- | :---------------------------------------------------------- |
|1.1| fib_series  |```lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])```|
|1.2| isFibonacci |  ```lambda x: True if x in source else False```  |
|1.3| filterFibonacciInList  |  ```list(filter(lambda x: True if x in source else False,l))```     |
|2.1| addEvenOdd  |  ```[a+b for a,b in zip(filter(lambda x: x%2 == 0, l1), filter(lambda x: x%2 == 1, l2))]```     |
|2.2| removeVowel  |  ```''.join([x for x in str if x.lower() not in {'a','e','i','o','u'}])```     |
|2.3| sigmoid  |  ```[round(1 / (1 + math.exp(-x)),2) for x in weights]```     |
|2.4| shiftEncoder  |  ```"".join([chr(int((ord(i) + 5 - 97)%26 )+97) for i in str])```     |
|3| findBadWords  |  ```[x for x in paragraph.lower().split() if x in [line.decode("utf-8").replace("\n","") for line in urllib.request.urlopen(url)]]```     |
|4.1| addEvenNumbers  |  ```reduce(lambda a,b:a+b,[x for x in l if x%2==0])```     |
|4.2| findBiggestCharacter  |  ```reduce(lambda a,b:a if ord(a)>ord(b) else b,str.lower())```     |
|4.3| addThirdNumber  |  ```reduce(lambda a,b: a+b,l[2::3])```     |
|5| generateNumberPlates  |  ```(['KA'+str(random.randint(10,99))+chr(random.randint(65,90))+chr(random.randint(65,90))+str(random.randint(1000,9999)) for x in range(limit)])```     |
|6.1| generateNumberPlatesOption  |  ```([stateCode.upper()+str(random.randint(10, 99))+chr(random.randint(65,90))+chr(random.randint(65,90))+str(random.randint(start,end)) for x in range(limit)])```     |
|6.2| generateNumberPlatesPartial |  ```partial(generateNumberPlatesOption,start = 2222,end = 3333)```  |



