import unittest

def obtener_cant_de_palabras_palindrome(word_list):
    result = 0
    for i in word_list:
        i = only_letters(i)
        if is_palindrome(i) == True:
            result += 1
    return result

def only_letters(word_phrase):
    word_phrase = word_phrase.lower()
    word_phrase = "".join(i for i in word_phrase if i.isalpha())
    return word_phrase

def is_palindrome(word):
    word = word.lower()
    for i in range(len(word)):
        if word[i] != word[-(i + 1)]:
            return False
    return True

class TestCantidad(unittest.TestCase):
    def test_cantidad_de_palabras_palindromes_simple(self):
        palabras = ["ala"]
        resultado = obtener_cant_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 1)

    def test_cantidad_de_palabras_palindromes_con_2(self):
        palabras = ["ala", "neuquen"]
        resultado = obtener_cant_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_3(self):
        palabras = ["ala", "neuquen", "hola"]
        resultado = obtener_cant_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_4(self):
        palabras = ["ala", "neuquen", "hola", "programacion"]
        resultado = obtener_cant_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_5(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap"]
        resultado = obtener_cant_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 3)

    def test_cantidad_de_palabras_palindromes_complejo(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap", "neu  quen"]
        resultado = obtener_cant_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 4)

    def test_cantidad_de_palabras_palindromes_complejo_2(self):
        palabras = [
            "ala",
            "neuquen",
            "hola",
            "programacion",
            "palap",
            "neu  quen",
            "agita falsos usos la fatiga",
            "presidente de la camara de diputados: martin menem",
            "A man, a plan, a canal - Panama"
        ]
        resultado = obtener_cant_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 6)

unittest.main()