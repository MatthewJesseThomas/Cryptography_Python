from cryptography.fernet import Fernet
# Encryption_Key
key = Fernet.generate_key()
print(key)

# Load Content of CSV file into memory
f = Fernet(key)
with open('sample.csv','rb') as orig_file:
    original = orig_file.read()
# Encryption
encrypted = f.encrypt(original)
# write encrypted content to a file
with open ('Sample_en.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
    
# Load Content of file into memory
f = Fernet(key)
with open('Sample_en.csv','rb') as encrypted_file:
    encrypted = encrypted_file.read()

# write decrypted content to a file
decrypted = f.decrypt(encrypted)
with open('Sample_de.csv', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)