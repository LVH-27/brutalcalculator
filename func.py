hello_string = "Hello and welcome to ICM summer of code"

for i in range(len(hello_string[0:15])):
	print(hello_string[i::] + hello_string[0:i])

print()


def funkcija(a=0, b=0):
	print("pozvana je funkcija za zbrajanje: {}*{}".format(a, b))

	return a * b

def eksp(eksponent):
	print("pozvana je funkcija za eksponencijranje")
	return math.exp(eksponent)
