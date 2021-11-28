import secrets
import base64

g = secrets.randbits(160)
p = secrets.randbits(80)

a = secrets.randbits(10)
b = secrets.randbits(10)

A = (g ** a) % p
B = (g ** b) % p

keyA = str((B ** a) % p).encode()
keyB = str((A ** b) % p).encode()

key1 = base64.b64encode(keyA)
key2 = base64.b64encode(keyB)

print(key1)
print(key2)

print(f"\nRESULT = {key1 == key2}")
