# 🔐 Caesar Cipher using Polynomial Hash

# Hash Function
def get_hash(key):
    p = 31
    m = 10**9 + 7
    hash_value = 0

    for ch in key:
        hash_value = (hash_value * p + ord(ch)) % m

    return hash_value


# Encryption
def encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.islower():
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        elif ch.isupper():
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += ch
    return result


# Decryption
def decrypt(text, shift):
    result = ""
    for ch in text:
        if ch.islower():
            result += chr((ord(ch) - ord('a') - shift + 26) % 26 + ord('a'))
        elif ch.isupper():
            result += chr((ord(ch) - ord('A') - shift + 26) % 26 + ord('A'))
        else:
            result += ch
    return result


# Utility function (used by test file)
def process(text, key):
    hash_value = get_hash(key)
    shift = hash_value % 26

    encrypted = encrypt(text, shift)
    decrypted = decrypt(encrypted, shift)

    return hash_value, shift, encrypted, decrypted