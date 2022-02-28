def decrypt_rsa(ct: int, d: int, n: int) -> int:
    """RSA decryption

    Args:
        ct (int): ciphertext
        d (int): private key
        n (int): modulus

    Returns:
        int: plaintext
    """
    return pow(ct, d, n)
