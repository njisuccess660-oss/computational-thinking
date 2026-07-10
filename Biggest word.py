"""
enter sentence

words = sentence.split()
while(len(sentence)>=1) then
print(sentence[i])
longest_word = max(words, key=len)

print longest_word
"""

# sentence = input("Enter a sentence: ")
# i = 1
# while(len(sentence)>=i):
#    words = sentence.split()
#    longest_word = max(words, key = len)
#    i += 1
# print(longest_word)    


# def max_word(sentence):
#    words = sentence.split()
#    longest = max(words, key = len)
#    return longest


# input_sentence = input("Enter the sentence: ")
# longest = max_word(input_sentence)
# print(longest)

name = "Nji Sunny Royce"
# name_split = name.split()
# name_rev=name[::-1]
# name_rev = name_rev.join()
# print(name_rev)
# rrcecar

word = input("Enter palindrome word to test: ")
if word == word[::-1]:
   print("Is palindrome")
else: 
   print("It's not!")