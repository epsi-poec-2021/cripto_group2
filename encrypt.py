import string
import sys
import unidecode


n = int(sys.argv[1])
message = sys.argv[2:]
message = message[0]
print(message)
message = message.upper()

message_crypt = []

for character in message:
  if character in string.ascii_uppercase:
    message_crypt += [chr((ord(character) + n) % 26)]

message_crypt = "".join(message_crypt)

print(message_crypt)
