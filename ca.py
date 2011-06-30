#!/usr/bin/env python

from bitstring import BitArray
from copy import copy

def g1():
    return _g1

def g2():
    return _g2

def g2i(i):
    return _g2i[i]

def _gen_g1():
    lfsr = BitArray(10)
    lfsr.set(True)

    seq = BitArray(1023)

    for i in range(1023):
        incoming_bit = lfsr[2] ^ lfsr[9]
        outgoing_bit = lfsr[9]
        lfsr.ror(1)
        lfsr[0] = incoming_bit
        seq[i] = outgoing_bit
    return seq

_g1 = _gen_g1()

def _gen_g2():
    lfsr = BitArray(10)
    lfsr.set(True)

    seq = BitArray(1023)

    for i in range(1023):
        incoming_bit = lfsr[1] ^ lfsr[2] ^ lfsr[5] ^ lfsr[7] ^ lfsr[8] ^ lfsr[9]
        outgoing_bit = lfsr[9]
        lfsr.ror(1)
        lfsr[0] = incoming_bit
        seq[i] = outgoing_bit
    return seq

_g2 = _gen_g2()

def _gen_g2i(i):
    n = [5, 6, 7, 8, 17, 18, 139, 140, 141, 251, 252, 254, 255, 256, 257, 258,
         469, 470, 471, 472, 473, 474, 509, 512, 513, 514, 515, 516, 869, 860,
         861, 862, 863, 950, 947, 948, 950]

    g2 = copy(_g2)
    g2.ror(n[i-1])
    g2i = _g1 ^ g2

    return g2i

_g2i = {}
for i in range(1, 37+1):
    _g2i[i] = _gen_g2i(i)

