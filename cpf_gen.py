import itertools 
import os
import sys

#Validate the CPF number against the rule from RFB
def validaCpf(cpf,d1=0,d2=0,i=0):
	while i<10:
		d1,d2,i=(d1+(int(cpf[i])*(11-i-1)))%11 if i<9 else d1,(d2+(int(cpf[i])*(11-i)))%11,i+1
	return (int(cpf[9])==(11-d1 if d1>1 else 0)) and (int(cpf[10])==(11-d2 if d2>1 else 0))

#Generate a combinatory analysis in the CPF format [XXX.XXX.XXX-XX]
#In this implementation we hava only the 6 numbers in the middle 
def TestaCPF(vlr_teste):
	for vlr_pre in range(0,1000):
		for vlr_pos in range(0,99):
			cpf =  str(vlr_pre).zfill(3) + str(vlr_teste) + str(vlr_pos).zfill(2)
			#print("% ; %", cpf ,validaCpf( cpf ))
			if 	validaCpf( cpf ):
				print cpf



if __name__ == '__main__':
	os.system('cls')
	
	#Testing
	TestaCPF("133568")
	TestaCPF("733974")
	TestaCPF("615337")
	TestaCPF("984447")
	TestaCPF("753327")	


