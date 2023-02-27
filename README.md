# These scrips are the result of the readings and tests using the tutorial found at: https://www.tutorialspoint.com/python-support-for-gzip-files-gzip

## GZip
The GZip application is used for compression and decompression of files.
It is a part of GNU project.
Python’s gzip module is the interface to GZip application.
The gzip data compression algorithm itself is based on zlib module.
The gzip module contains definition of GzipFile class along with its methods.
It also caontains convenience functions open(), compress() and decompress().
The easiest way to achieve compression and decompression is by using the above mentioned functions.
 
## open()
This function opens a gzip-compressed file in binary or text mode and returns a file like object,
which may be a physical file, a string or a byte object.
By default, the file is opened in ‘rb’ mode i.e. reading binary data, however, the mode parameter to this function can take other modes as listed below.
binary mode: 'r', 'rb', 'a', 'ab', 'w', 'wb', 'x', 'xb'
text mode : 'rt', 'at', 'wt', or 'xt'
This function also defines compression level whose acceptable value is between 0 to 9.
When the file is opened in text mode, the GzipFile object is wrapped in TextIOWrapper object.

## compress()
This function applies compression on the data given to it as argument and returns a compressed byte object.
By default compression level is 9.

## decompress()
This function decompresses the byte object and returns uncompressed data.
