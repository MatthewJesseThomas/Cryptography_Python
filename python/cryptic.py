import string

plain_text = "Secret#0001"
shift = 0

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift] 
table = str.maketrans(alphabet, shifted)

encrypted = plain_text.translate(table)
print(encrypted)

