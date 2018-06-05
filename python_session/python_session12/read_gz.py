import gzip

with gzip.open("file.txt.gz", "rb") as f:
	print f.read()
