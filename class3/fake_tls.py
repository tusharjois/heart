from signature import signature
from key_exchange import key_exchange
from encryption import encryption

identity = "proof of being Bob"
msg_to_send = "secret plans for world domination"

# Digital signature
if signature(identity):
    print("\n----\n")

    # Key exchange
    alice_K, bob_K = key_exchange()
    print("\n----\n")

    # Encrypted application communication 
    encryption(msg_to_send, alice_K, bob_K)
