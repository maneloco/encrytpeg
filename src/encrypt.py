from typing import List, Tuple
from .utils import get_character_table

def to_number(message: str) -> bytearray:
    table, _ = get_character_table()
    nums: List[int] = [table[char] for char in message]
    return bytearray(nums)

def from_number(numbers: bytearray) -> str:
    _, reverse = get_character_table()
    nums: List[int] = list(numbers)
    result: str= ""
    for num in nums:
        result += reverse[num]
    return result


def xor_encryption(message: str, key: str) -> Tuple[str, List[bytearray]]:
    message_bytes = to_number(message)
    key_bytes = to_number(key)
    encrypted_message = bytearray()

    i = 0
    j = 0
    while i < len(message_bytes):
        xor = message_bytes[i] ^ key_bytes[j]
        encrypted_message.append(xor)
        i += 1
        j = (j + 1) % len(key_bytes)
    
    return encrypted_message, key_bytes

def xor_decryption(message_encrypted: bytearray, key: bytearray) -> Tuple(str, str):
    decrypted_message = bytearray()
    _, reverse = get_character_table()

    i = 0
    j = 0
    while i < len(message_encrypted):
        xor = message_encrypted[i] ^ key[j]
        decrypted_message.append(xor)
        i += 1
        j = (j + 1) % len(key)
    return from_number(decrypted_message), from_number(key)

