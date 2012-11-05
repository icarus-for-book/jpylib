#!/usr/bin/env python

'''\
This is program which can convert binary to c/c++ code.

author: jinsub ahn <jinniahn@gmail.com>

usage: 
   $> python bin2code.py <in-file> [<out-file>]

   - <in-file>  : the file path to convert ( required )
   - <out-file> : out file path to save conveted code 
                  if not, it will be printed on console

   
'''

import os
import sys

def usageAndExit(code):
    print '''\
This is program which can convert binary to c/c++ code.

author: jinsub ahn <jinniahn@gmail.com>

usage: 
   $> python bin2code.py <in-file> [<out-file>]

   - <in-file>  : the file path to convert ( required )
   - <out-file> : out file path to save conveted code 
                  if not, it will be printed on console
'''
    exit(code)

def main(args):
    
    if len(args) == 0: 
        usageAndExit(1)

    # get in,out file
    try:
        infile = open(args[0],'rb')
    except:
        print 'cannot open input file'
        usageAndExit(1)
    try:
        outfile = open(args[1],'w')
    except:
        outfile = sys.stdout

    # covert binaray code to hexstring
    hexdatas = []
    count = 0
    indata = infile.read()
    for ch in indata:
        if count % 10 == 0:
            hexdatas.append("\n     '\\x%02x'" % ord(ch))
        else:
            hexdatas.append("'\\x%02x'" % ord(ch))            
        count += 1

    code = []
    code.append('char bindata[] = { ')
    code.append(', '.join(hexdatas))
    code.append('};\n')
    code.append('int bindata_size = %d;' % len(indata))

    outfile.write(''.join(code))

if __name__ == '__main__':
    main(sys.argv[1:])

