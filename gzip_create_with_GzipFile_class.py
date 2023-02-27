# In addition to the convenience functions (open, read, and write),
# gzip module also has GzipFile class which defines the compress() and decompress() methods.
# The constructor of this class takes file, mode and compressionlevel arguments.
# When mode parameter is given as ‘w’ or ‘wb’ or ‘wt’, the GipFile object will provide write() method to compress the given data and write to a gzip file.
# This will create a testnew.txt.gz file.
# You can unzip it using any utility to see that it contains testnew.txt with ‘Python – Batteries included’ text in it.
import gzip

f = gzip.GzipFile("testnew.txt.gz","wb")
data = b'Python - Batteries included'
f.write(data)
f.close()
