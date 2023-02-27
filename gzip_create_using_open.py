# open()
# This function opens a gzip-compressed file in binary or text mode and returns a file like object,
# which may be a physical file, a string or a byte object.
# By default, the file is opened in ‘rb’ mode i.e. reading binary data, however, the mode parameter to this function can take other modes as listed below.
# binary mode: 'r', 'rb', 'a', 'ab', 'w', 'wb', 'x', 'xb'
# text mode : 'rt', 'at', 'wt', or 'xt'
# This function also defines compression level whose acceptable value is between 0 to 9.
# When the file is opened in text mode, the GzipFile object is wrapped in TextIOWrapper object.
# 
# The following example creates a gzip file by writing compressed data in it.
# This will create “test.txt.gz” file in current directory.
# This gzip archive contains “test.txt” which you can verify using any unzipping utility.
import gzip

data = b'Python - Batteries included'
with gzip.open("test.txt.gz", "wb") as f:
    f.write(data)
