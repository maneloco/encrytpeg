import unittest

from src.utils import get_character_table

class TestCrearTablas(unittest.TestCase):
    def test_longitud_reverse_table(self):
        _, reverse_table = get_character_table()
        longitud = len(reverse_table.keys())
        self.assertEqual(longitud, 256, "La tabla no tiene valores para mezclar el mensaje.")

    def test_se_ha_revertido(self):
       characters, reverse = get_character_table()
       for caracter, numero in characters.items():
           if numero <= 97:
               self.assertEqual(
                       reverse[numero], 
                       caracter, 
                       f"Fallo en el índice {numero}: se esperaba '{caracter}' pero se obtuvo '{reverse[numero]}'"
                       )    

    def test_tiene_caracteres_especiales(self):
        characters, _ = get_character_table()
        self.assertEqual(characters["ñ"], 26)
        self.assertEqual(characters[" "], 96)
        self.assertEqual(characters["\0"], 97)

if __name__ == "__main__":
    unittest.main()
