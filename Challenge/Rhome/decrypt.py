from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from hashlib import sha256
from sympy.ntheory import discrete_log


def decrypt(encrypted_flag, ss):
    key = sha256(long_to_bytes(ss)).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    pt = cipher.decrypt(encrypted_flag)
    return f"flag = {pt}"

def main():
    encrypted_flag = bytes.fromhex(input("Enter encrypted_flag: "))
    p = int(input("Enter p: "))
    g = int(input("Enter g:"))
    A = int(input("Enter A:"))
    B = int(input("Enter B:"))
    b = pow(g, 1, p)
    a = discrete_log(p,A,b)
    ss = pow(B, a, p)
    print(decrypt(encrypted_flag, ss))
    
if __name__ == "__main__":
    main()
