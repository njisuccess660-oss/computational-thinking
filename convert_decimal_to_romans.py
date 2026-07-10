""" 
input decimal num
romans = [M, CM, D, CD, C, XC, L, XL, X, IX, V, IV, I]
Values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 1]
result = ''
i=0
while (num>i) then
    while(num>=values)the
    result+=romans
    num-=values
    endwhile
    i+=1
    endwhile
 
 print result   
"""
def convert_to_dec():
    num = int(input("Enter number to be converted : "))
    romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ''
    i=0
    while num > 0:
        while num >= values[i]:
            result += romans[i]
            num -= values[i]
        i += 1    
    print(result)
       
convert_to_dec()
            