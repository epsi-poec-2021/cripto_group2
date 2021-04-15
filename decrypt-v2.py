import sys
key = sys.argv[1].upper()
message = sys.argv[2].upper()
encrypted_message = ""
coefficient = len(message) // len(key)
number_character_remaining = len(message) % len(key)
key_good_length = coefficient * key + key[:number_character_remaining]
message_size = len(message)
for i in range(message_size):
	shift = ord(key_good_length[i]) % ord('A') 
	encrypted_index_letter =  ord(message[i])  - shift # only this line changed in comparison to encrypt-v2.py
	encrypted_character = chr(encrypted_index_letter) 
	encrypted_message += encrypted_character

print(encrypted_message) 