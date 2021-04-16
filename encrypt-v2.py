import sys
import string

def delete_space_punctuation(message):
	message_without_punctuation = ""
	for character in message:
		if character in string.ascii_uppercase:

			message_without_punctuation += character

	return message_without_punctuation

def create_key_length_equal_to(message, key):
	coefficient = len(message) // len(key)
	number_character_remaining = len(message) % len(key)
	key_good_length = coefficient * key + key[:number_character_remaining]
	
	return key_good_length

def encrypt(message, key_good_length):
	message_size = len(message)
	encrypted_message = ""
	for i in range(message_size):
		shift = ord(key_good_length[i]) % ord('A') 
		encrypted_index_letter =  ord(message[i])  + shift 
		if encrypted_index_letter > ord('Z'):
			encrypted_index_letter = encrypted_index_letter % ord('Z') + ord('A') - 1
		encrypted_character = chr(encrypted_index_letter) 
		encrypted_message += encrypted_character

	return encrypted_message

def main():
	key = sys.argv[1].upper()
	message = sys.argv[2].upper()
	message = delete_space_punctuation(message)
	key_good_length = create_key_length_equal_to(message, key)
	encrypted_message = encrypt(message, key_good_length)
	print(encrypted_message)


main()