#Enter list of nums
#Enter target num
#for num in ramge len(nums)
# if (num[i]+num[i+1]==target_num){
# print(num[i])
# print(num[i+1])
#numbers = input("Enter a list of numbers")
#numbers = [int(x) for x in numbers.split(",")]
#print(numbers)
#numbers = list(map(int, input("Enter a list of numbers(spaced-seperated):").split()))
"""def find_two_sums(numbers, target_num):
    num_dic = {}
    for i in range(len(numbers)-1):
      complement = target_num - numbers[i]
    if complement in num_dic:
        return [num_dic[complement], i]
    num_dic[numbers[i]] = i
    return "no pairs found"
numbers = input("enter numbers")
numbers = [int(x) for x in numbers.split()]
target_num = int(input("enter target number"))
print(find_two_sums(numbers, target_num))
"""
def find_two_numbers(nums, target):
    for i in range(len(nums)):
        for j in range (i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return "no pair found"    

nums = list(map(int, input("enter numbers").split()))
target = int(input("enter target number"))    
print(find_two_numbers(nums, target))