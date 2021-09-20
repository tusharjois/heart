from nacl.public import PrivateKey, Box
from base64 import b64encode


def key_exchange():
    # Alice: generate a secret a and public A, and send A -> Bob 
    secret_a = PrivateKey.generate()
    print("Alice has generated a: " + b64encode(secret_a._private_key).decode('ascii'))
    public_A = secret_a.public_key
    print("Alice is sending A: {} to Bob...".format(b64encode(public_A._public_key).decode('ascii')))
    print()

    # Bob: generate a secret b and public B, and send B -> Alice
    secret_b = PrivateKey.generate()
    print("Bob has generated b: " + b64encode(secret_b._private_key).decode('ascii'))
    public_B = secret_b.public_key
    print("Bob is sending B: {} to Alice...".format(b64encode(public_B._public_key).decode('ascii')))
    print()

    # Bob: receive public A from Alice, and compute the shared secret K using A and b,
    bob_K = Box(secret_b, public_A)
    print("Bob uses A and b to generate secret key: " + b64encode(bob_K.shared_key()).decode('ascii'))
    print()

    # Alice: receive public B from Alice, and compute the shared secret K using B and a
    alice_K = Box(secret_a, public_B)
    print("Alice uses B and a to generate secret key: " + b64encode(alice_K.shared_key()).decode('ascii'))
    print()

    if alice_K.shared_key() == bob_K.shared_key():
        print("Alice and Bob now have the same shared secret, K!")
    else:
        print("Oh no! Something went wrong...")

    return alice_K, bob_K
