import spongent
import binascii
import time

mystr="Sponge + Present = Spongent"
m=int(binascii.hexlify(mystr.encode()),16)

print ("Message:\t",mystr)

#start=time.perf_counter()
start1=time.perf_counter_ns()
spongent80 =  spongent.SPONGENT(n=88, c=80, r=8, R=45)
print ("SPONGENT-088-080-008:\t",hex(spongent80.hash(m, prefix_zeros=1)))
#end=time.perf_counter()
end1=time.perf_counter_ns()
#print ("Time(sec): ",(end-start))
print ("Time(ms): ",((end1-start1)/1000000))
print()

#start=time.perf_counter()
start1=time.perf_counter_ns()
spongent128 = spongent.SPONGENT(n=128, c=128, r=8, R=70)
print ("SPONGENT-128-128-008:\t",hex(spongent128.hash(m, prefix_zeros=1)))
#end=time.perf_counter()
end1=time.perf_counter_ns()
#print ("Time(sec): ",(end-start))
print ("Time(ms): ",((end1-start1)/1000000))
print()

#start=time.perf_counter()
start1=time.perf_counter_ns()
spongent160 = spongent.SPONGENT(n=160, c=160, r=16, R=90)
print ("SPONGENT-160-160-016:\t",hex(spongent160.hash(m, prefix_zeros=1)))
#end=time.perf_counter()
end1=time.perf_counter_ns()
#print ("Time(sec): ",(end-start))
print ("Time(ms): ",((end1-start1)/1000000))
print()

#start=time.perf_counter()
start1=time.perf_counter_ns()
spongent224 = spongent.SPONGENT(n=224, c=224, r=16, R=120)
print ("SPONGENT-224-224-016:\t",hex(spongent224.hash(m, prefix_zeros=1)))
#end=time.perf_counter()
end1=time.perf_counter_ns()
#print ("Time(sec): ",(end-start))
print ("Time(ms): ",((end1-start1)/1000000))
print()

#start=time.perf_counter()
start1=time.perf_counter_ns()
spongent256 = spongent.SPONGENT(n=256, c=256, r=16, R=140)
print ("SPONGENT-256-256-016:\t",hex(spongent256.hash(m, prefix_zeros=1)))
#end=time.perf_counter()
end1=time.perf_counter_ns()
#print ("Time(sec): ",(end-start))
print ("Time(ms): ",((end1-start1)/1000000))
print()
