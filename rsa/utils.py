def egcd(a: int,  b: int) -> tuple[int, int, int]:
    """Extended Euclidean algorithm

    Args:
        a (int): integer
        b (int): integer

    Returns:
        tuple[int, int, int]: (gcd, x, y) where gcd = gcd(a, b), x = a * y + b * x, y = b * y - a * x
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a: int, m: int) -> int:
    """Modular inverse

    Args:
        a (int): integer
        m (int): modulus

    Raises:
        Exception: if a is not coprime to m

    Returns:
        int: modular inverse of a mod m
    """
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def generate_keys(p: int, q: int) -> tuple[int, int, int]:
    """Generate RSA keys

    Args:
        p (int): prime number 1
        q (int): prime number 2

    Returns:
        tuple[int, int, int]: (e, d, n) where e = public key, d = private key, n = pq
    """
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = modinv(e, phi)
    return (e, d, n)


def str2long(s: str) -> int:
    """Convert string to integer

    Args:
        s (str): string

    Returns:
        int: integer
    """
    return int.from_bytes(s.encode(), 'big')


def long2str(n: int) -> str:
    """Convert integer to string

    Args:
        n (int): integer

    Returns:
        str: string
    """
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
