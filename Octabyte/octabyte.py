OCTABYTEARR = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@#"
print(len(OCTABYTEARR))

def octabyte(decNum:int):
    octabyteVal = ""
    if (decNum==0):
        return "4x0"
    while(decNum > 0):
        remainder = decNum % 64
        octabyteVal = (OCTABYTEARR[remainder]) + octabyteVal
        decNum //= 64
    return "4x" + octabyteVal

def octabyte_to_dec(num:str):
    decVal = 0
    pureNum = num[2:]
    iter = 1
    for e in pureNum[::-1]:
        decVal += OCTABYTEARR.find(e) * iter
        iter *= 64
    return decVal

def dec(num:str):
    if num[0:2].lower() == "4x":
        return octabyte_to_dec(num)
    elif num[0:2].lower() == "0x":
        return int(num, 16)
    elif num[0:2].lower() == "0b":
        return int(num, 2)
    else:
        print(f"Undefined format: [{num}]. ")
        return None
        



test_list = [0, 1, 15, 16, 30, 31, 32, 33, 128, 500, 1000, 4000, 9999, 1000000000000000000000000, 0xfffffffffffffffffffff]
for e in test_list:
    print(e, " - ", octabyte(e), " - ", dec(octabyte(e)))
    assert dec(octabyte(e)) == dec(hex(e))
    assert dec(octabyte(e)) == dec(bin(e))
    assert dec(octabyte(e)) == e
    assert dec(hex(e)) == e
    assert dec(bin(e)) == e
print("all passed")

print(octabyte(15557293025018116))
