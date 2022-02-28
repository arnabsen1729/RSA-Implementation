def encrypt_rsa(pt: int, e: int, n: int) -> int:
    """RSA encryption

    Args:
        pt (int): plaintext
        e (int): public key
        n (int): modulus

    Returns:
        int: ciphertext
    """
    return pow(pt, e, n)
