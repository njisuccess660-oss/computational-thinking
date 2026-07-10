"""
enter number
how to get factors of a number
output those that are prime
select the laggest prime
"""
num = int(input("Enter number"))
i= 2
prime_factors = []
while num >= i*i:
    if(num % i == 0):
        prime_factors.append(i)      
        num // i
    else:
        i += 1
if num >1: prime_factors.append(num)       
print(prime_factors)