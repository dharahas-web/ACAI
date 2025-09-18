import unittest

def is_palindrome(text: str) -> bool:
    """
    Checks if the given string is a palindrome, ignoring case and non-alphanumeric characters.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the cleaned string is a palindrome, False otherwise.
    """
    # Fix: include digits (isalnum), and make it case-insensitive (lower)
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

class TestIsPalindrome(unittest.TestCase):
    def test_palindrome_with_punctuation(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_palindrome_with_numbers(self):
        self.assertTrue(is_palindrome("12321"))

    def test_mixed_case_and_symbols(self):
        self.assertTrue(is_palindrome("No 'x' in Nixon!"))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_two_different_characters(self):
        self.assertFalse(is_palindrome("ab"))

if __name__ == "__main__":
    # Let the user provide input
    user_input = input("Input: ")
    print("Output: - Task_2.py:42", is_palindrome(user_input))
    # Optionally, run unit tests
    # unittest.main()