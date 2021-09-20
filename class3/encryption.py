from base64 import b64encode

def encryption(msg, alice_K, bob_K):
    print("Alice is going to encrypt {} to Bob.".format(msg))

    # Alice: use a shared secret to encrypt and send a message 
    encrypted = alice_K.encrypt(msg.encode('utf-8'))
    print("Encrypted {} to Bob.".format(b64encode(encrypted).decode('ascii')))
    
    # Bob: receive the message and decrypt it using the shared secret
    print()
    print("Bob is going to decrypt {} from Alice.".format(b64encode(encrypted).decode('ascii')))
    decrypted = bob_K.decrypt(encrypted).decode('utf-8')
    print("Decrypted {} from Alice.".format(decrypted))

    print()
    if msg == decrypted:
        print("Success!")
    else:
        print("Oh no! Something went wrong...")
