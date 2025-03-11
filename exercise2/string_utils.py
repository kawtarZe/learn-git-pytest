def reverse_string(s: str) -> str:
    """
    Return the input string in reverse order.
    """
    return s[::-1]

def count_vowels(s: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    Case-insensitive: both uppercase and lowercase vowels should be counted.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def is_palindrome(s: str) -> bool:
    """
    Check if the input string is a palindrome.
    A palindrome reads the same backward as forward.
    Spaces and case should be ignored.
    """
    filtered_s = ''.join(char.lower() for char in s if char.isalnum())
    return filtered_s == filtered_s[::-1]

def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the input string.
    """
    return s.title()