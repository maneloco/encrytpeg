import random

def get_character_table():
    character_table = dict()

    for i in range(26):
        character_table[chr(i + 97)] = i

    character_table['ñ'] = 26

    for i in range(26):
        character_table[chr(i + 65)] = i + 27
    character_table['Ñ'] = 53

    for i in range(31):
        character_table[chr(i + 33)] = i + 54

    for i, tilde in enumerate(["á", "é", "í", "ó", "ú", "Á", "É", "Í", "Ó", "Ú"]):
        character_table[tilde] = i + 85

    character_table['\n'] = 95
    character_table[' '] = 96
    character_table['\0'] = 97

    reverse_table = dict()
    for key, value in character_table.items():
        reverse_table[value] = key

    for i in list(range(98, 256)):
        reverse_table[i] = random.choice(list(character_table.keys()))
    
    return character_table, reverse_table
