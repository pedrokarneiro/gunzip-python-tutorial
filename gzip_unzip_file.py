# To retrieve the uncompressed file from gzip archive
# This code will create ‘zen1.txt’ in the current directory which contains the same data as in ‘zen.txt’.
import gzip

# To uncompress an existing gzip archive into a file...
fp = open("zen1.txt", "wb")              # Open file object to be written to
with gzip.open("zen.txt.gz", "rb") as f: # Read from the gzipped file...
    bindata = f.read()                   # ...into a binary object
fp.write(bindata)                        # Write to the file object
fp.close()                               # Close the file object
