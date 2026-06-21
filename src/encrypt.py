from typing import List, Tuple
from .utils import get_character_table

def to_number(message: str) -> bytearray:
    table, _ = get_character_table()
    nums: List[int] = [table[char] for char in message]
    return bytearray(nums)

def from_number(numbers: bytearray) -> str:
    _, reverse = get_character_table()
    nums: List[int] = list(numbers)
    result: str = "".join([reverse[num] for num in numbers])
    return result


def xor_encryption(message: str, key: str) -> Tuple[str, List[bytearray]]:
    message_bytes = to_number(message)
    key_bytes = to_number(key)
    encrypted_message = xor_operation(message_bytes, key_bytes)
    
    return encrypted_message, key_bytes

def xor_decryption(message_encrypted: bytearray, key: bytearray) -> Tuple(str, str):
    decrypted_message = xor_operation(message_encrypted, key)

    return from_number(decrypted_message), from_number(key)


def xor_operation(bytes_a: bytearray, bytes_b: bytearray) -> bytearray:
    result = bytearray()
    i, j = 0, 0
    while i < len(bytes_a):
        xor = bytes_a[i] ^ bytes_b[j]
        result.append(xor)
        i += 1
        j = (j + 1) % len(bytes_b)
    return result

