#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import getopt
import codecs

def find_next_letter(dst, letter, pos=0):
    if pos == 0:
        postfix = ''
    else:
        postfix = str(pos)
    
    search_str = letter + postfix
    
    if search_str in dst:
        find_next_letter(dst, letter, pos+1)
    else:    
        dst.add(search_str)


def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hvd:a:l:', ['help', 'dictionary=','alphabet=','length='])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    dictionary = None
    verbose = False
    alphabet = None
    length = None

    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-d", "--dictionary"):
            dictionary = a
        elif o in ("-a", "--alphabet"):
            alphabet = a.decode(sys.stdin.encoding)
        elif o in ("-l", "--length"):
            length = int(a)
        else:
            assert False, "unhandled option"

    if dictionary is None:
        dictionary = 'russian'
    
    if alphabet is None:
            assert False, "undefined alphabet"
    
    if length is None:
            assert False, "undefined length"

    dst = set()

    for letter in alphabet:
        find_next_letter(dst, letter)
    
    with codecs.open('dictionaries/'+dictionary, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if len(line) != length:
                continue
            line_set = set()
            for letter in line:
                find_next_letter(line_set, letter)
    
            if line_set.issubset(dst):
                print line.encode('utf-8')

if __name__ == "__main__":
    main()
