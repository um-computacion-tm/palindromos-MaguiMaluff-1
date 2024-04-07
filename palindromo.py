import unittest

"""def is_palindrome(word):
    word = word.lower()
    reverse = word[::-1]
    if word == reverse:
        return True
    else:
        return False"""

def is_palindrome(word):
    word = word.lower()
    for i in range(len(word)):
        if word[i] != word[-(i + 1)]:
            return False
    return True

class TestIsPalindrome(unittest.TestCase):
    def test_with_a(self):
        word = "a"
        result = is_palindrome(word)
        self.assertTrue(result)
    
    def test_with_ala(self):
        word = "ala"
        result = is_palindrome(word)
        self.assertTrue(result)
    
    def test_with_pan(self):
        word = "pan"
        result = is_palindrome(word)
        self.assertFalse(result)
    
    def test_with_aleteo(self):
        word = "aleteo"
        result = is_palindrome(word)
        self.assertFalse(result)

    def test_with_1345(self):
        word = "1345"
        result = is_palindrome(word)
        self.assertFalse(result)

    def test_with_NeuQuEn(self):
        word = "NeuQuen"
        result = is_palindrome(word)
        self.assertTrue(result)

    def test_with_neuquen(self):
        word = "neuquen"
        result = is_palindrome(word)
        self.assertTrue(result)

unittest.main()