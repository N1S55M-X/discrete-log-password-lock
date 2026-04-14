# Discrete Logarithm Password Lock

This repository demonstrates an **educational proof‑of‑concept** for password verification using modular exponentiation and the discrete logarithm problem. It shows how a password can be transformed into a "lock value" that is easy to compute but hard to reverse.

## Concept
- A password is hashed with SHA‑256 and converted to an integer.
- A lock value is computed as `y = g^x mod p`, where `p` is a large prime and `g` is a generator.
- Verification checks whether recomputing the lock with the given password matches the stored value.

## Research Connections
This simple idea is the root of many complex cryptographic systems:
- **Diffie–Hellman Key Exchange**: Securely establish shared secrets over the internet.
- **ElGamal Encryption**: Public‑key encryption based on discrete logs.
- **Digital Signature Algorithm (DSA)**: Used for secure digital signatures.
- **Elliptic Curve Cryptography (ECC)**: A modern variant using points on elliptic curves, powering secure messaging, cryptocurrencies, and TLS.
- **Zero‑Knowledge Proofs**: Advanced protocols where one party proves knowledge of a secret without revealing it, often built on discrete log hardness.

These projects scale the same principle you see here — exponentiation is easy, discrete logs are hard — into full systems that secure web traffic, blockchain transactions, and digital identities.

## Usage
```bash
pip install -r requirements.txt

