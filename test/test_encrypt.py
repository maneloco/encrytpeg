import unittest
from typing import List
from src.encrypt import to_number, from_number, xor_encryption

class TestEncriptacion(unittest.TestCase):
    def test_from_text_to_numbers(self):
        message: str = "Amartelada"
        nums: bytearray = to_number(message)
        message_from_nums: str = from_number(nums)
        self.assertEqual(message, message_from_nums, "La función no convierte el mensaje a bytes bien.")  

    def test_xor_encryption(self):
        message: str = "Amartelada"
        key: str = "FP2"
        encrypted_message, returned_key = xor_encryption(message, key)
        self.assertEqual(to_number(key), returned_key, "La función no devuelve la key correctamente")
        decrypted_message, key = xor_encryption(encrypted_message, key)
        self.assertEqual(message, decrypted_message, "La función no encripta bien el mensaje")

if __name__ == "__main__":
    unittest.main()

