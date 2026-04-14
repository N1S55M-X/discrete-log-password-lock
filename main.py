# Install PyCryptodome if needed
# !pip install pycryptodome

from Crypto.Util import number
import hashlib
import secrets

# Step 1: Generate a large prime p and a generator g
# For demo: 256-bit prime (use 2048+ bits in practice!)
p = number.getPrime(256, randfunc=secrets.token_bytes)
g = 2  # simple generator candidate

print("Prime p:", p)
print("Generator g:", g)

# Step 2: Encode password into integer using SHA-256
def password_to_int(password: str) -> int:
    h = hashlib.sha256(password.encode()).hexdigest()
    return int(h, 16)

# Step 3: Create lock
def create_lock(password: str, g: int, p: int) -> int:
    x = password_to_int(password)
    return pow(g, x, p)

# Step 4: Verify password
def verify_password(password: str, lock: int, g: int, p: int) -> bool:
    return create_lock(password, g, p) == lock

# --- Test the system ---
password = "mySecret123"
lock = create_lock(password, g, p)

print("\nLock value (store this safely):", lock)

# Correct password check
print("Verify correct password:", verify_password("mySecret123", lock, g, p))

# Wrong password check
print("Verify wrong password:", verify_password("wrongPass", lock, g, p))
