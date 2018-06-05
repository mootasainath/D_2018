import sys

name=sys.argv[1]

if name == name[::-1]:
	print("polyndrome")
else:
	print("Not a polyndrome")
