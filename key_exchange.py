from Crypto import Random
from Crypto.Cipher import AES
import secrets

g = secrets.randbits(160)
p = secrets.randbits(80)

a = secrets.randbits(10)
b = secrets.randbits(10)

A = (g ** a) % p
B = (g ** b) % p

keyA = str((B ** a) % p).encode()
keyB = str((A ** b) % p).encode()

key1 = keyA.hex()
key2 = keyB.hex()

print(f"KEY 1 = {key1}")
print(f"KEY 2 = {key2}")

print(f"\nKEY EQUALITY RESULT = {key1 == key2}\n")

def pad(data):
        return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

def encrypt_str(data, key):
    data = bytes(data.encode("utf-8"))
    data = pad(data)
    iv = Random.new().read(AES.block_size)
    enc = AES.new(key, AES.MODE_CBC, iv)

    return iv + enc.encrypt(data)

def decrypt_str(ciphertext, key):
    ciphertext = bytes.fromhex(ciphertext)
    iv = ciphertext[:AES.block_size]
    dec = AES.new(key, AES.MODE_CBC, iv)
    plaintext = dec.decrypt(ciphertext[AES.block_size:])

    return plaintext.rstrip(b"\0")

common_data = "hello world"

cipher1 = encrypt_str(common_data, bytes.fromhex(key1)).hex()
cipher2 = encrypt_str(common_data, bytes.fromhex(key2)).hex()

print(f"CIPHER 1 = {cipher1}")
print(f"CIPHER 2 = {cipher2}")

plain1 = decrypt_str(cipher1, bytes.fromhex(key1))
plain2 = decrypt_str(cipher1, bytes.fromhex(key2))

print(f"\nPLAIN-TEXT 1 = {plain1.decode('utf-8')}")
print(f"PLAIN-TEXT 2 = {plain2.decode('utf-8')}")

print(f"\nPLAIN-TEXT EQUALITY RESULT = {plain1 == plain2}\n")
