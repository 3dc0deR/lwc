# https://asecuritysite.com/encryption/chas2
import chas
import time

k='chaskey is a mac'
p='message part 1'

print ("Message: ",p)
print ("Key: :",k)

k = k.rjust(16, ' ') # we need 16 byte for the key - 128 bits

#start=time.perf_counter()
start1=time.perf_counter_ns()
# 16 byte signature
instance = chas.chaskey(k.encode(),16,p.encode())
#end=time.perf_counter()
end1=time.perf_counter_ns()

#print ("Time(sec): ",(end-start))
print ("Time(ms): ",((end1-start1)/1000000))
print("Signature:", instance.digest().hex())
