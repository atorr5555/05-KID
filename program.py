import sys
import fileinput

entrada = []
# Recibe la entrada
for line in fileinput.input():
	entrada.append(line)

entrada = list(map(lambda x : x.replace('\n', ''), entrada))
action = entrada[0]
a = int(entrada[1])
b = int(entrada[2])
A = int(entrada[3])
B = int(entrada[4])
message = int(entrada[5])

M = (a * b) - 1
e = (A * M) + a
d = (B * M) + b
n = ((e * d) - 1) / M


if action == 'E':
	# Encrypt
	print(int((message * e) % n))
else:
	# Decrypt
	print(int((message * d) % n))