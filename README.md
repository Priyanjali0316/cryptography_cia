# Caesar Cipher using Custom Polynomial Hash Function

## Overview

This project implements a Caesar Cipher encryption and decryption system using a custom polynomial rolling hash function. The hash function dynamically generates a shift value based on a user-provided key.

---

## Theory

### Caesar Cipher

The Caesar Cipher is a substitution cipher where each character in the plaintext is shifted by a fixed number of positions.

Encryption:
C = (P + k) mod 26

Decryption:
P = (C - k) mod 26

---

### Hash Function

A hash function converts a key (string) into a numeric value.

In this project, we use a **Polynomial Rolling Hash**:

hash = (hash × p + ASCII) mod m

Where:

* p = 31 (prime number)
* m = 10⁹ + 7

The final shift value is:
shift = hash mod 26

---

## ⚙️ Working

1. User enters plaintext and key
2. Key is converted into a hash value
3. Hash value is reduced to a shift (0–25)
4. Caesar cipher is applied using the shift
5. Same shift is used to decrypt the text

---

## ▶️ How to Run

```bash
python crypto.py
```

---

## 📊 Example 1

Plaintext: hello
Key: abc

Hash Value: 96354
Shift: 24

Encrypted: fcjjm
Decrypted: hello

---

## Example 2

Plaintext: world
Key: data

Hash Value: 3076010
Shift: 2

Encrypted: yqtnf
Decrypted: world

---

## Round-Trip Verification

The program ensures:
plaintext → encryption → decryption → original text

✔ Round-trip successful in all test cases

---

## Notes

* Different hash functions produce different shift values
* Therefore, encrypted output may vary for the same input
* The shift is limited to 26 values (alphabet size)

---

## ✅ Conclusion

This implementation demonstrates how a hash function can be combined with a classical encryption technique to dynamically generate keys, making the cipher more flexible than a fixed-shift Caesar Cipher.
