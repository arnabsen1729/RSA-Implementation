from rsa import utils, encrypt, decrypt


def main():
    while True:
        print("RSA Encryption/Decryption")
        print("=========================")
        print("")
        print("Choose an option:")
        print("1. Generate new keys")
        print("2. Encrypt a message")
        print("3. Decrypt a message")
        print("4. Exit")
        print("")
        option = input("Option: ")
        if option == "1":
            p = utils.generate_large_prime(128)
            q = utils.generate_large_prime(128)
            print("")
            print("Generating primes...")
            print("p: {}".format(p))
            print("q: {}".format(q))
            e, d, n = utils.generate_keys(p, q)
            print("")
            print("Public key: (e, n) = ({}, {})".format(e, n))
            print("Private key: (d, n) = ({}, {})".format(d, n))
            print("")
        elif option == "2":
            e = int(input("Public key (e): "))
            n = int(input("Public key (n): "))
            m = utils.str2long(input("Message: "))
            c = encrypt.encrypt_rsa(m, e, n)
            print("Encrypted message: {}".format(c))
            print("")
        elif option == "3":
            d = int(input("Private key (d): "))
            n = int(input("Private key (n): "))
            c = int(input("Ciphertext: "))
            m = utils.long2str(decrypt.decrypt_rsa(c, d, n))
            print("Decrypted message: {}".format(m))
            print("")
        else:
            print("\nby Arnab Sen (510519006)")
            break


if __name__ == "__main__":
    main()
