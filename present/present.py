from pypresent import Present
import Padding
import sys
import time

text="help"
k="00000000000000000000"

if (len(sys.argv)>1):
	text=str(sys.argv[1])

if (len(sys.argv)>2):
	k=str(sys.argv[2])



print ('Text:\t'+text)
print ('Key:\t'+k)
print ('--------')
print
key = bytes.fromhex(k)
   
text = Padding.appendPadding(text,blocksize=8,mode='CMS')

cipher = Present(key) 

#start=time.perf_counter()
start1=time.perf_counter_ns()
encrypted = cipher.encrypt(text.encode())
#end=time.perf_counter()
end1=time.perf_counter_ns()

#print ("Encrypt time(sec): ",(end-start))
print ("Encrypt time(ms): ", ((end1-start1)/1000000))

print ('Cipher(Hex Encoded):\t'+encrypted.hex())
#start=time.perf_counter()
start1=time.perf_counter_ns()
decrypted = cipher.decrypt(encrypted)
#end=time.perf_counter()
end1=time.perf_counter_ns()

#print ("Decrypt time(sec): ",(end-start))
print ("Decrypt time((ms): ", ((end1-start1)/1000000))

print ('Decrypted(Hex encoded):\t'+decrypted.hex())
print ('Decrypted:\t'+Padding.removePadding(decrypted.decode(),blocksize=8,mode='CMS'))
