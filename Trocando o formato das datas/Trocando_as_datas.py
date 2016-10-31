import shutil, os, re
datePattern = re.compile(r"""(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$""", re.VERBOSE)
# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    if mo == None:
        continue
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

datePattern = re.compile(r"""^(1) (2 (3))- (4 (5))- (6 (7) ) (8)$ """, re.VERBOSE)

# Form the European-style filename.
euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

# Get the full, absolute file paths.
absWorkingDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkingDir, amerFilename)
euroFilename = os.path.join(absWorkingDir, euroFilename)

# Rename the files.
print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
# shutil.move(amerFilename, euroFilename) # uncomment after testing