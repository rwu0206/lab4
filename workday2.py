#Problem 4

def isPalindrome(x):
    if int(x[::-1]) == int(x):
        return True

palindromes = []
for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        product = x*y
        if isPalindrome(str(product)):
            palindromes.append(product)
print(max(palindromes))
