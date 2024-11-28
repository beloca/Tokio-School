import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Paso 1: Generar las claves RSA
key = RSA.generate(2048, e=65537)  # Longitud de clave 2048, exponente 65537
private_key = key
public_key = key.publickey()

private_pem = private_key.export_key()
public_pem = public_key.export_key()

print("Clave privada:")
print(private_pem.decode())
print("\nClave pública:")
print(public_pem.decode())

# Paso 2: Texto a cifrar
text = "ESTAMOS EN CLASE DE CRIPTOGRAFIA."
print("\nTexto original:")
print(text)

# Paso 3: Cifrar con la clave pública
rsa_cipher = PKCS1_OAEP.new(public_key)  # cifrado con clave pública
ciphertext = rsa_cipher.encrypt(text.encode())  # Cifrar el texto

print("\nTexto cifrado (en bytes):")
print(ciphertext)

# Paso 4: Desencriptar con la clave privada (opcional, para verificar)
decipher = PKCS1_OAEP.new(private_key)  
decrypted_text = decipher.decrypt(ciphertext).decode()

print("\nTexto descifrado:")
print(decrypted_text)