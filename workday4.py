#Problem 6

sum1 = 0 #sum of the numbers squared
sum2 = 0 #square of sum of the numbers
for x in range(101):
    sum1 += x**2 #adding all the squared numbers from 1-100

for i in range(101):
    sum2 += i #adding all of the numbers together
sum2 = sum2**2 #squaring the sum

print(sum2-sum1)


#Problem 7 (IN PROGRESS)

count = 0
num = 0

while count != 10001:
    bruh = True
    for i in range(2, num):

        if num % i == 0:
            bruh = False
            break
    if bruh == False:
        num += 1
    else:
        num +=1
        count +=1

print(num)


