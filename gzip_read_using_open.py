# To programmatically read this compressed file, use this code:
import gzip

with gzip.open("test.txt.gz", "rb") as f:
    data = f.read()
print(data)

# The output should be: b'Python - Batteries included'
