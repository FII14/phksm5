#!/usr/bin/env python3

import hashlib
import time
import sys
import os

print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ Program : Pemecah hash kata Sandi  MD5    @
@ Pembuat : Rofi [FII14]                    @
@ GitHub  : https://github.com/FII14/pkshm5 @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""")

hash = input("Masukkan hash MD5 yang ingin dipecahkan: ")

if len(hash) != 32:
    print(f"Kesalahan: Hash '{hash}' tidak valid.")
    sys.exit(1)

file_wordlist = input("Masukkan path ke file wordlist: ")

if not os.path.exists(file_wordlist):
    print(f"Kesalahan: File wordlist '{file_wordlist}' tidak ditemukan.")
    sys.exit(1)

with open(file_wordlist, 'r', encoding='latin-1', errors='ignore') as w:
    daftar_kata = w.read().splitlines()

for kata_sandi in daftar_kata:
    hash_kata_sandi = hashlib.md5(kata_sandi.encode()).hexdigest()
    
    if hash_kata_sandi == hash:
        print(f"\n[*] Hash MD5: {hash}\n[*] Kata sandi: {kata_sandi}\n[*] Status: Benar\n")
        break
        sys.exit(0)

    else:
        print(f"\n[*] Hash MD5: {hash}\n[*] Kata sandi: {kata_sandi}\n[*] Status: Salah")
    time.sleep(1)

else:
    print("\nKata sandi tidak ditemukan dalam file wordlist '{file_wordlist}'.")
    sys.exit(1)
