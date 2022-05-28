first_word = input("Enter the first word: ")

second_word = input("Enter the second word: ")

first_word = first_word.strip(" ")

second_word = second_word.strip(" ")

first_word_set = set(first_word)

second_word_set = set(second_word)

if first_word_set == second_word_set:
    print("These words are anagrams of each other")
else:
    print("These words are not anagrams of each other")
