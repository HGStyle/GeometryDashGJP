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

This repo is only to learn you what is GJP and how to generate it.
Because here is no many sites that learn you that.
Enjoy generating GJP !

# Credits
Credits to tildeman (https://github.com/tildeman/) with his repository `getGJP` at https://github.com/tildeman/getGJP

Credits to Cvolton (https://github.com/Cvolton/) with his repository `GMDprivateServer` at https://github.com/Cvolton/GMDprivateServer

Credits to Geometry Dash Documentation Team for XOR cipher and Base64 encode functions. Unofficial Geometry Dash Docs by them at :
New GD Docs: https://docs.gd-programming.org/
Old GD Docs backup: https://wyliemaster.github.io/gddocs/#/

Credits to me (i've converted the PHP code of @tildeman to Python code).
