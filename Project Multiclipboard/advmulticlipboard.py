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
elif len(sys.argv) == 6 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
    for number in list[::1]:
        del list[number]

mcbShelf.close()
