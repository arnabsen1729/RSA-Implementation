from rsa import utils, encrypt, decrypt

message = "Hello World"
print(message)
p = 41786401492786869780779898241890479177074358209493
q = 50645864855555557158850899875137062695990384997089
e, d, n = utils.generate_keys(p, q)
print(f"e: {e}")
print(f"d: {d}")
print(f"n: {n}")

pt = utils.str2long(message)
ct = encrypt.encrypt_rsa(pt, e, n)
print(f"pt: {pt}")
print(f"ct: {ct}")

pt2 = decrypt.decrypt_rsa(ct, d, n)
print(f"pt2: {pt2}")
print(f"{utils.long2str(pt2)}")
