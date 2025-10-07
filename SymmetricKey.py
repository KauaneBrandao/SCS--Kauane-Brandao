from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

key = RSA.generate(2048)
publicKey = key.publickey()
cipher = PKCS1_OAEP.new(publicKey)

message = input("Digite a sua mensagem: ")
ciphertext = cipher.encrypt(message.encode())

print("Criptografado:", base64.b64encode(ciphertext).decode())

decipher = PKCS1_OAEP.new(key)
decryption = decipher.decrypt(ciphertext).decode()

print("Descriptografado:", decryption)
