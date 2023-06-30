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

if __name__ == "__main__":
    pw = input('GD Password (will be echoed) : ')
    gjp = generate_gjp(pw)
    print(f'GJP is : {gjp}')
