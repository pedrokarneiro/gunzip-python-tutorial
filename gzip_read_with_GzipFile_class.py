# To uncompress the gzip file using GzipFile object,create it with ‘rb’ value to mode parameter and read the uncompressed data by read() method
import gzip

f = gzip.GzipFile("testnew.txt.gz","rb")
data = f.read()
print(data)

# The output should be: b'Python - Batteries included'