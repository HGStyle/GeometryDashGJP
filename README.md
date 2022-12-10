# What is Geometry Dash GJP ?

GJP is for "Geometry Jump Password".
To generate GJP from user password, you need :
 1. The password as string
 2. Encipher it with XOR with key "37526"
 3. Encode it with Base64 with URLSafe

Here is a Python function to generate GJP:
```python
import base64
import itertools

def base64_encode(string: str) -> str:
    return base64.urlsafe_b64encode(string.encode()).decode()

def xor_cipher(string: str, key: str) -> str:
    return ("").join(chr(ord(x) ^ ord(y)) for x, y in zip(string, itertools.cycle(key)))

def generate_gjp(password: str):
	  gjp = xor_cipher(password, "37526")
	  gjp = base64_encode(gjp)
	  return gjp

pw = input('GD Password (will be echoed) : ')
gjp = generate_gjp(pw)
print('GJP is : ' + gjp)
```
