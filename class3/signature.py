from nacl.signing import SigningKey
from base64 import b64encode

# Bob: generate a key pair
def signature(msg):
    bob_signature_key = SigningKey.generate()
    print("Bob has generated a signing key: " + b64encode(bob_signature_key._signing_key).decode('ascii'))

    # Bob: use the secret key to sign a message
    signed = bob_signature_key.sign(msg.encode('utf-8'))
    print("Bob has signed {} as {}.".format(msg, b64encode(signed).decode('ascii')))

    # Bob: send the public key, message, and tag to the Client
    bob_verify_key = bob_signature_key.verify_key
    print()
    print("Alice will use {} to verify {}.".format(b64encode(bob_verify_key._key).decode('ascii'), b64encode(signed).decode('ascii')))

    # Alice: verify that the tag validates for the message 
    if bob_verify_key.verify(signed):
        print("The verification passed!")
        return True
    else:
        print("Oh no! Something went wrong...")
        return False

