challenge : http://www.loyalty.org/~schoen/rsa/challenge.zip
    
    
from Crypto.Util.number import long_to_bytes,bytes_to_long
from Crypto.PublicKey import RSA 
import os 

L =os.listdir()
list_file = []
list_pubKeys=[]


def gcdExtended(a, b):
	if a == 0:
		return b, 0, 1

	gcd, x1, y1 = gcdExtended(b % a, a)

	x = y1 - (b//a) * x1
	y = x1
	return gcd ,x ,y


for file in L :
	if os.path.isfile(file) and file != "test.py" and file.split(".")[-1] =="pem" :
		list_file.append(file)
def get_d(phi,e):
    number=gcdExtended(phi,e)[2]
    if number<0:
        return number +phi
    else:
        return number


for file in list_file :
	with open(file, 'r') as file :
		a = file.read()
		list_pubKeys.append(RSA.importKey(a).n)
		

for i in range (len(list_pubKeys)):
	for j in range (i+1,len(list_pubKeys)-1):
		if gcdExtended(list_pubKeys[i],list_pubKeys[j])[0] != 1:
			print(f"the two public keys in file {list_file[i]} and {list_file[j]} are not coprime and their gcd is :\n[*] {gcdExtended(list_pubKeys[i],list_pubKeys[j])[0]} ")
			str1 = list_file[i].split('.')[0]
			str_=str1 +'.bin'
			with open(str_ , 'rb') as file :
				binary_text = file.read()
			p_1 = gcdExtended(list_pubKeys[i],list_pubKeys[j])[0]
			q_1 = list_pubKeys[i] // gcdExtended(list_pubKeys[i],list_pubKeys[j])[0]
			phi =(p_1-1)*(q_1-1)
			d = get_d(phi,65537)
			m=pow(bytes_to_long(binary_text),d,list_pubKeys[i])
			print(f"[*] file {str_} has been decrypted successfully : {long_to_bytes(m)}")
			str2 = list_file[j].split('.')[0]
			str_=str2 +'.bin'
			with open(str_ , 'rb') as file :
				binary_text = file.read()
			p_1 = gcdExtended(list_pubKeys[i],list_pubKeys[j])[0]
			q_1 = list_pubKeys[j] // gcdExtended(list_pubKeys[i],list_pubKeys[j])[0]
			phi =(p_1-1)*(q_1-1)
			d = get_d(phi,65537)
			m=pow(bytes_to_long(binary_text),d,list_pubKeys[j])
			print(f"[*] file {str_} has been decrypted successfully : {long_to_bytes(m)}")
      
      
      Solution : Virgile 
