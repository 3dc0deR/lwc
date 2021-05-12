from os import urandom
from eccsnacks.curve25519 import scalarmult, scalarmult_base
import binascii
from timeit import default_timer as timer

# Based on code from https://github.com/nnathan/eccsnacks/blob/master/eccsnacks/curve25519.py

start=timer()

lamb = urandom(32)
a = scalarmult_base(lamb)

eps = urandom(32)
b = scalarmult_base(eps)

c = scalarmult(eps, a)

d = scalarmult(lamb, b)

end=timer()

print "RFID private key: ",binascii.hexlify(eps)

print "Reader private key: ",binascii.hexlify(lamb)

print
print "A value: ",binascii.hexlify(a)
print "B value: ",binascii.hexlify(b)

print "C value: ",binascii.hexlify(c)
print "D value: ",binascii.hexlify(d)

print
print "Check that C is equal to D"
print "Time(ms): ",(end-start) * 1000
