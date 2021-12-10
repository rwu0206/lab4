#Problem 1

from math import *

numlist = [] #creating an empty list to hold all of the numbers that fit the conditions
for x in range(1000): #finding all numbers that fit the conditions
    if x % 3 == 0:
        numlist.append(x) #adding to the list
    elif x % 5 == 0:
        numlist.append(x)

sum = 0 #final number
for x in numlist: #adding all numbers from the list to the final sum
    sum = sum + x

print(sum)
       
            
#Problem 2

fib = [] #establishing variables
num = 1
add = 0
fibsum = 0

while fibsum < 4000000: #making sure the final number is below 40000000
    fibsum = num + add
    add = num # number 2 becomes the number after the last number 2
    num = fibsum # number 1 becomes the number aftert the last number 1
    fib.append(fibsum) #add all numbers to a list

sum = 0
for x in fib: #adding all even numbers together
    if x % 2 == 0:
        sum = sum + x

print(sum)


#Problem 3

primes = [] #empty list of primes

for x in range(600851475143): #run through every number
    num = 1
    factorcount = 0
    while num <= x: #PRIME CHECK
        if x % num == 0: #finding a factor 
            factorcount += 1
        num = num+1
    if factorcount == 2: #prime numbers only have 2 factors, so if the numebr being examined only has 2, it is considered a prime
        primes.append(x)


print(primes[-1]) #print the last number in the list (the largest)
        
            
