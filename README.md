# Caesar Cipher using Custom Polynomial Hash Function

## 📌 Overview

This project implements a Caesar Cipher encryption and decryption system using a custom polynomial rolling hash function. The hash function dynamically generates a shift value based on a user-provided key.

The project is structured into:

* `cipher.py` → Contains hashing, encryption, and decryption logic
* `test.py` → Contains test cases demonstrating functionality

---

## Theory

### Caesar Cipher

The Caesar Cipher is a substitution cipher where each character is shifted by a fixed number of positions.

Encryption:
C = (P + k) mod 26

Decryption:
P = (C - k) mod 26

---

### Hash Function

A hash function converts a key (string) into a numeric value.

This implementation uses a **Polynomial Rolling Hash**:

hash = (hash × p + ASCII) mod m

Where:

* p = 31 (prime number)
* m = 10⁹ + 7

Final shift:
shift = hash mod 26

---

## ⚙️ Working

1. Input plaintext and key
2. Compute hash value from key
3. Generate shift using modulo 26
4. Encrypt plaintext using Caesar cipher
5. Decrypt ciphertext using same shift

---

## ▶️ How to Run

### Step 1: Make sure both files are in the same folder

```
cipher.py
test.py
```

### Step 2: Run the test file

```bash
python test.py
```

---

## 📊 Test Cases

### Example 1

Plaintext: hello
Key: abc

Hash Value: 96354
Shift: 24

Encrypted: fcjjm
Decrypted: hello

---

### Example 2

Plaintext: world
Key: data

Hash Value: 3076010
Shift: 2

Encrypted: yqtnf
Decrypted: world

---

## 🔁 Round-Trip Verification

The system verifies:
plaintext → encryption → decryption → original text

✔ All test cases successfully return the original text

---

##  Notes

* Different keys produce different hash values and shifts
* Final shift is limited to 26 (alphabet size)
* This is not a secure cryptographic system but demonstrates core concepts

---

## ✅ Conclusion

This project shows how hashing can be integrated with classical encryption techniques to dynamically generate encryption keys, improving flexibility over fixed-shift Caesar Cipher.


<img width="938" height="523" alt="image" src="https://github.com/user-attachments/assets/1a284cb0-f1cc-4ab5-b33d-35a16c30895e" />

## Prompts
Give algorithm and code for implementing Caesar cipher using hashing and hash function with explanation.
Are there collisions in this hash function?
Explain hashing and hash functions in detail.
Give an improved hash function with better distribution.
Explain polynomial rolling hash with example.
Provide step-by-step algorithm for encryption and decryption using hash-based Caesar cipher.
Why is my output different?
Help debug incorrect shift value and encryption result.
