from numpy import *

def g1():
    return _g1

def g2():
    return _g2

def g2i(i):
    return _g2i[i]

def _gen_g1():
    lfsr = ones(10, dtype=uint8)

    seq = empty(1023, dtype=uint8)

    for i in range(1023):
        incoming_bit = lfsr[2] ^ lfsr[9]
        outgoing_bit = lfsr[9]
        lfsr = roll(lfsr, 1)
        lfsr[0] = incoming_bit
        seq[i] = outgoing_bit
    return seq

_g1 = _gen_g1()

def _gen_g2():
    lfsr = ones(10, dtype=uint8)

    seq = empty(1023, dtype=uint8)

    for i in range(1023):
        incoming_bit = lfsr[1] ^ lfsr[2] ^ lfsr[5] ^ lfsr[7] ^ lfsr[8] ^ lfsr[9]
        outgoing_bit = lfsr[9]
        lfsr = roll(lfsr, 1)
        lfsr[0] = incoming_bit
        seq[i] = outgoing_bit
    return seq

_g2 = _gen_g2()

def _gen_g2i(i):
    n = [5, 6, 7, 8, 17, 18, 139, 140, 141, 251, 252, 254, 255, 256, 257, 258,
         469, 470, 471, 472, 473, 474, 509, 512, 513, 514, 515, 516, 859, 860,
         861, 862, 863, 950, 947, 948, 950]

    g2 = roll(_g2, n[i-1])
    g2i = _g1 ^ g2

    return g2i

_g2i = [None]
for i in range(1, 37+1):
    _g2i.append(_gen_g2i(i))

def _int_to_bits(num):
    bits = empty(0, dtype=uint8)
    while num > 0:
        bits =append(bits, num & 1)
        num >>= 1
    return bits[::-1]

