#!/usr/bin/env python

import bitstring as bs

def gen_g1():
    lfsr = bs.BitArray(10)
    lfsr.set(True)
    
    seq = bs.BitArray(1023)

    for i in range(1023):
        incoming_bit = lfsr[2] ^ lfsr[9]
        outgoing_bit = lfsr[9]
        lfsr.ror(1)
        lfsr[0] = incoming_bit
        seq[i] = outgoing_bit
    return seq

def gen_g2():
    lfsr = bs.BitArray(10)
    lfsr.set(True)

    seq = bs.BitArray(1023)

    for i in range(1023):
        incoming_bit = lfsr[1] ^ lfsr[2] ^ lfsr[5] ^ lfsr[7] ^ lfsr[8] ^ lfsr[9]
        outgoing_bit = lfsr[9]
        lfsr.ror(1)
        lfsr[0] = incoming_bit
        seq[i] = outgoing_bit
    return seq

def gen_g2i(i):
    n= [5, 6, 7, 8, 17, 18, 139, 140, 141, 251, 252, 254, 255, 256, 257, 258,
        469, 470, 471, 472, 473, 474, 509, 512, 513, 514, 515, 516, 869, 860,
        861, 862, 863, 950, 947, 948, 950]

    g1 = gen_g1()
    g2 = gen_g2()
    g2.ror(n[i-1])
    g2i = g1 ^ g2

    return g2i

