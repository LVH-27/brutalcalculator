from math import sqrt

hello_string = "Hello and welcome to ICM summer of code"

for i in range(len(hello_string[0:15])):
	print(hello_string[i::] + hello_string[0:i])

print()


def zbroji(a=0, b=0):
    print("pozvana je funkcija za zbrajanje: {}+{}".format(a, b))

    return a + b

def oduzmi(a=0,b=0):
	print("pozvana je funkcija za oduzimanje: {}-{}".format(a, b))
	return a-b 

