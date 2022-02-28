def encrypt_rsa(pt: int, e: int, n: int) -> int:
    return pow(pt, e, n)
