#from ca_prng import *
import ca_prng
from numpy import *

def int_to_bits_test():
    gold = array((1,1,0,0,1,0,0,0,0,0), dtype=uint8)
    bits = ca_prng._int_to_bits(01440)
    assert (gold == bits).all()

def g2i_test():
    first_ten = (
        None,
        01440,
        01620,
        01710,
        01744,
        01133,
        01455,
        01131,
        01454,
        01626,
        01504,
        01642,
        01750,
        01764,
        01772,
        01775,
        01776,
        01156,
        01467,
        01633,
        01715,
        01746,
        01763,
        01063,
        01706,
        01743,
        01761,
        01770,
        01774,
        01127,
        01453,
        01625,
        01712,
        01745,
        01713,
        01134,
        01456,
        01713,
    )
    for i in range(1, len(first_ten)):
        gold = ca_prng._int_to_bits(first_ten[i])
        bits = ca_prng.g2i(i)
        print "prn: %d first 10 chips (octal): %s" % (i, oct(first_ten[i]))
        print "gold: %s" % str(gold)
        print "bits: %s" % str(bits[:10])
        assert (gold == bits[:10]).all()

