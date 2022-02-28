def decrypt_rsa(ct: int, d: int, n: int) -> int:
    return pow(ct, d, n)
