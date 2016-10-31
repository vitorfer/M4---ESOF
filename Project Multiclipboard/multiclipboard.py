#! /usr/bin/env python3
#usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
 #       py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
 #       py.exe mcb.pyw list - Loads all keywords to clipboard.
 # py -2 -m pip install SomePackage 
 # default Python 2 py -2.7 -m pip install SomePackage 
 # specifically Python 2.7 py -3 -m pip install SomePackage 
 # default Python 3 py -3.4 -m pip install SomePackage 
 # specifically Python 3.4

import shelve 
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
     # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pypertclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
