def Check_word_is_plaindrome():
     word_pilandrom =input("Please enter a word: ")
     new_word=word_pilandrom.lower().replace(" ","")
     if new_word[::1] == new_word[::-1]:
        print("Given string is Palindrome")
     else:
        print("NOT A Palindrome String")
        
Check_word_is_plaindrome()        