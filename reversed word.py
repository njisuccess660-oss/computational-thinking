def reversed_string(word):
 word_reverse = ""
 for i in range(len(word_input)-1, -1, -1):
        word_reverse += word[i]
 return word_reverse
word_input = input("Enter a string :")
print(reversed_string(word_input))    
        
