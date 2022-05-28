# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment]

    first_word_set = set(word)

    second_word_set = set(anagram)

    if first_word_set == second_word_set:
        return True
    else:
        return False

value = find_anagram("hello", "check")
print(value)

value = find_anagram("below", "elbow")
print(value)
