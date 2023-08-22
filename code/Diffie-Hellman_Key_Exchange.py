import random

# Common parameters, publicly known
g = 5 # Primitive root modulo of 23
p = 23 # Prime number

#Alice and Bob generate their private and public keys
def generate_keys():
    private_key = random.randint(1, p)
    public_key = (g ** private_key) % p #g^private_key mod p
    return private_key, public_key

# Alice
a_private, A_public = generate_keys()

# Bob
b_private, B_public = generate_keys()

# Exchange public keys amd compute shared secret
def compute_shared_secret(private_key, public_key):
    return (public_key ** private_key) % p # public_key^private_key mod p

# Alice computes shared secret
alice_secret = compute_shared_secret(a_private, B_public)

# Bob computes shared secret
bob_secret = compute_shared_secret(b_private, A_public)

print("Alice's Shared Secret:", alice_secret)
print("Bob's Shared Secret:", bob_secret)
