from typing import List, Tuple
from .utils import get_character_table

def to_number(message: str) -> bytearray:
    table, _ = get_character_table()
    nums: List[int] = [table[char] for char in message]
    return bytearray(nums)

def from_number(numbers: List[bytearray]) -> str:
    _, reverse = get_character_table()
    nums: List[int] = list(numbers)
    result: str= ""
    for num in nums:
        result += reverse[num]
    return result


def xor_encryption(message: str, key: str) -> Tuple[str, List[bytearray]]:
    message_bytes = to_number(message)
    key_bytes = to_number(key)
    _, reverse = get_character_table()
    encrypted_message = bytearray()

    i = 0
    j = 0
    while i < len(message_bytes):
        xor = message_bytes[i] ^ key_bytes[j]
        encrypted_message.append(xor)
        i += 1
        j += 1
        if j == len(key_bytes):
            j = 0
    
    return from_number(encrypted_message), key_bytes

