#Problem 5


num = 20 #first number tested
got = False 
while got == False: #while loop ending when the number is gotten
    count = 0 #how many times it is divided evenly
    for div in range(1,21): #for loop from 1-20
        if num % div == 0: #dividing by numbers from 1-20
            count += 1 #when it is evenly divisible, it will add one to the count
    if count == 20: #if it is divisible by all numbers 1-20
        print(num) #show number
        got == True #stop loop
    num += 1 #if not, test next number


    



