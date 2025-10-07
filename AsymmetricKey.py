from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

key = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_EAX)

text = input("Digite a sua mensagem: ")
encryptiontext, tag = cipher.encrypt_and_digest(text.encode())

print("Mensagem Criptografada", base64.b64encode(encryptiontext).decode())

# Descriptografia
encryption= AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decryption= encryption.decrypt(encryptiontext).decode()

print("Mensagem Original:", decryption)
