import random

g = 5
p = 23

def generate_private_key():
    return random.randint(1, p)

def compute_public_key(private_key):
    return (g ** private_key) % p

def compute_shared_secret(private_key, other_party_public_key):
    return (other_party_public_key ** private_key) % p

def mitm_attack():
    # Alice and Bob generate their private and public keys
    alice_private_key = generate_private_key()
    alice_public_key = compute_public_key(alice_private_key)

    bob_private_key = generate_private_key()
    bob_public_key = compute_public_key(bob_private_key)

    #John intercepts the public keys
    john_fake_key = generate_private_key()
    john_fake_public_key = compute_public_key(john_fake_key)

    # John sends his public key to both Alice and Bob, pretending to be the other party
    alice_believed_shared_secret = compute_shared_secret(alice_private_key, john_fake_public_key)
    bob_believed_shared_secret = compute_shared_secret(bob_private_key, john_fake_public_key)

    # John computes the shared secret with both Alice and Bob
    john_shared_secret_with_alice = compute_shared_secret(john_fake_key, alice_public_key)
    john_shared_secret_with_bob = compute_shared_secret(john_fake_key, bob_public_key)

    # Validate the attack
    assert alice_believed_shared_secret == john_shared_secret_with_alice
    assert bob_believed_shared_secret == john_shared_secret_with_bob
    print("Man-in-the-middle attack successful by John!")

mitm_attack()
