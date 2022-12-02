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