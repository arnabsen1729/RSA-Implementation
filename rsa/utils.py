import random
import math


def egcd(a: int,  b: int) -> tuple[int, int, int]:
    """Extended Euclidean algorithm

    Args:
        a (int): integer
        b (int): integer

    Returns:
        tuple[int, int, int]: (gcd, x, y) where gcd = gcd(a, b),
        x = a * y + b * x, y = b * y - a * x
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
        tuple[int, int, int]: (e, d, n)
        where e = public key, d = private key, n = pq
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


def rabin_miller(n: int) -> bool:
    """Rabin–Miller primality test is a probabilistic primality test: an
    algorithm which determines whether a given number is likely to be prime

    Args:
        n (int): integer

    Returns:
        bool: True if n is probably prime, False otherwise
    """
    s = n-1
    t = 0
    while s & 1 == 0:
        s = s//2
        t += 1
    k = 0
    while k < 128:
        a = random.randrange(2, n-1)
        v = pow(a, s, n)
        if v != 1:
            i = 0
            while v != (n-1):
                if i == t-1:
                    return False
                else:
                    i = i+1
                    v = (v**2) % n
        k += 2
    return True


def is_prime(n: int) -> bool:
    """Standard Prime Check

    lowPrimes is all primes (sans 2, which is covered by the bitwise and
    operator) under 1000. taking n modulo each lowPrime allows us to remove a
    huge chunk of composite numbers from our potential pool without resorting to
    Rabin-Miller

    Args:
        n (int): integer

    Returns:
        bool: True if n is probably prime, False otherwise
    """

    lowPrimes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    if (n >= 3):
        if (n & 1 != 0):
            for p in lowPrimes:
                if (n == p):
                    return True
                if (n % p == 0):
                    return False
            return rabin_miller(n)
    return False


def generate_large_prime(k: int) -> int:
    """Generate large prime number of length k

    Args:
        k (int): desired bit length

    Raises:
        Exception: If prime number cannot be found

    Returns:
        int: large prime number
    """
    r = 100*(math.log(k, 2)+1)  # number of attempts max
    r_ = r
    while r > 0:
        # randrange is mersenne twister and is completely deterministic
        # unusable for serious crypto purposes
        n = random.randrange(2**(k-1), 2**(k))
        r -= 1
        if is_prime(n):
            return n
    raise Exception(f"Failure after {r_} tries.")
