target_string = "yourexploitationisawesome"

print(target_string)
local_58 = list()
local_60 = 0

sVar1 = len(target_string)

print(sVar1)

while( True ):
    if(local_60 >= sVar1):
        break
    print(target_string[local_60])
    local_58.append(chr(ord(target_string[local_60]) ^ 0x45))
    local_60 = local_60 + 1

print("".join(local_58))
