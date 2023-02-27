# In the example below, ‘zen.txt’ file is assumed to be present in current directory.
import gzip

# To compress an existing file to a gzip archive...
fp = open("zen.txt","rb")                  # 1. open the file into a file object (here we call it fp)
data = fp.read()                           # 2. read text in the file object to a data object (here we call it data)
bindata = bytearray(data)                  # 3. convert the data object to bytearray (here we've put it into bindata)
with gzip.open("zen.txt.gz", "wb") as f:   # 4. This bytearray object is then written...
    f.write(bindata)                       # ...to a gzip file.

