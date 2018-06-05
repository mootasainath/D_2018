import bz2 
content = "Lots of content here"
with bz2.BZ2File('file.bz2', 'wb') as f:
    f.write(content)
