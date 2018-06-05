import bz2 

with bz2.BZ2File("file.bz2", "rb") as f:
	print f.read()
