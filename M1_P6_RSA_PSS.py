from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256

# 1. Generar las claves RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# 2. Crear un mensaje para firmar
message = b"ESTAMOS EN CLASE DE CRIPTOGRAFIA." #la b indica que no es str normal sino bytes

# 3. Crear un hash del mensaje
hash = SHA256.new(message)

# 4. Firmar el mensaje con la clave privada usando PSS
signature = pss.new(private_key).sign(hash)

print("Firma digital (en bytes):")
print(signature.hex())

# 5. Verificar la firma con la clave pública
verifier = pss.new(public_key)
try:
    verifier.verify(hash, signature)
    print("La firma es válida.")
except (ValueError, TypeError):
    print("La firma no es válida.")
