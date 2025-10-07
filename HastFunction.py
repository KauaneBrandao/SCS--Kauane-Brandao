import hashlib
message = input("Mensagem para o usuário: ")

hash_resultado = hashlib.sha256(message.encode()).hexdigest()
print("Hash SHA-256:", hash_resultado)
