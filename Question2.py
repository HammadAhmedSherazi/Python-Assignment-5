def count_upper_lower():
    lowercase_letter_count = 0
    uppercase_letter_count = 0
    string=input("Enter a string:")

    for letter in string:
        if letter.isupper():
            uppercase_letter_count += 1
        elif letter.islower():
            lowercase_letter_count += 1

    print ("No. of uppercase letters is",
    uppercase_letter_count, "and No. of lowercase letters is", lowercase_letter_count)

count_upper_lower()

