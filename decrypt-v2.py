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

def decrypt(message, key_good_length):
	message_size = len(message)
	decrypted_message = ""
	for i in range(message_size):
		shift = ord(key_good_length[i]) % ord('A') 
		decrypted_index_letter =  ord(message[i])  - shift 
		if decrypted_index_letter < ord('A'):
			#decrypted_index_letter can't be inferior to encrypted_index_letter - 25 (shift in beetween 0 at 25) 
			#Thus we don't need to add ord(Z) more than one time
			decrypted_index_letter = decrypted_index_letter - ord('A') + ord('Z') + 1 
		decrypted_character = chr(decrypted_index_letter) 
		decrypted_message += decrypted_character

	return decrypted_message

def main():
	key = sys.argv[1].upper()
	message = sys.argv[2].upper()
	message = delete_space_punctuation(message)
	key_good_length = create_key_length_equal_to(message, key)
	decrypted_message = decrypt(message, key_good_length)
	print(decrypted_message)


main()



