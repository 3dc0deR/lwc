from  trivium import Trivium
import binascii
import sys
import time


def _hex_to_bytes(s):
    return [_allbytes[s[i:i+2].upper()] for i in range(0, len(s), 2)]

def bits_to_hex(b):
    return "".join(["%02X" % sum([b[i + j] << j for j in range(8)]) for i in range(0, len(b), 8)])

def hex_to_bits(s):
    return [(b >> i) & 1 for b in _hex_to_bytes(s) for i in range(8)]

_allbytes = dict([("%02X" % i, i) for i in range(256)])
def get_next_stream_byte():
  rtn = 0
  for j in range(8):
    rtn+=int(next_key_bit()) << j;
  return rtn


_allbytes = dict([("%02X" % i, i) for i in range(256)])


message=b"hello"
k1="0F62B5085BAE0154A7FA"
i1="288FF65DC42B92F960C7"



if (len(sys.argv)>1):
	k1=str(sys.argv[1])

if (len(sys.argv)>2):
	i1=str(sys.argv[2])

if (len(sys.argv)>3):
	message=str(sys.argv[3]).encode()

print ("Key: "+k1)
print ("IV:  "+i1)

KEY = hex_to_bits(k1)[::-1]
IV = hex_to_bits(i1)[::-1]

#start=time.perf_counter()
start1=time.perf_counter_ns()

trivium = Trivium(KEY, IV)
next_key_bit = trivium.keystream().__next__
keystream = []
for j in range(128):
  keystream.append(next_key_bit())
print ("Key stream: "+bits_to_hex(keystream))

trivium = Trivium(KEY, IV)
next_key_bit = trivium.keystream().__next__

buffer=bytearray()
for mybyte in message:
    c=get_next_stream_byte()
    newbyte = (mybyte ^ c ) & 0xFF
    buffer.append(newbyte)

#end=time.perf_counter()
end1=time.perf_counter_ns()
	
# Reset key stream
trivium = Trivium(KEY, IV)
next_key_bit = trivium.keystream().__next__


decrypt=''

print ("\nPlaintext: ",message.decode())
print ("Cipher: ",binascii.hexlify(buffer))
print ("Encrypt time(ms): ",((end1-start1)/1000000))
#print ("Encrypt time(ns): ", (end1-start1))

#start=time.perf_counter()
start1=time.perf_counter_ns()

for mybyte in buffer:
  c=get_next_stream_byte()
  newbyte = (mybyte ^ c) & 0xFF
  decrypt+=chr(newbyte)
  
#end=time.perf_counter()
end1=time.perf_counter_ns()

print (f"Decrypted: {decrypt}")
print ("Decrypt time(ms): ",((end1-start1)/1000000))
#print ("Decrypt time(ns): ", (end1-start1))
