import string
import sys
import unidecode


n = int(sys.argv[1])
message = sys.argv[2]
message = message.upper()

cipher = ""

for character in message:
    if character in string.ascii_uppercase:
        ascii_code = ord(character)
        alpha_index = ascii_code - ord("A")  # between 0 and 25
        alpha_index = (alpha_index + n) % 26  # between 0 and 25
        encrypted_ascii_code = ord("A") + alpha_index
        encrypted_character = chr(encrypted_ascii_code)
        cipher += encrypted_character


print(cipher)
