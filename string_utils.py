def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")