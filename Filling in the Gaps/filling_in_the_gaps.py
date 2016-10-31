import shutil, os

barra = '\\'
print('FIRST YOU NEED TO SEARCH THE PATH OF THE FOLDER THAT YOU WANT TO COPY FILES WITH .pdf OR .jpg')
pathFolder = input('\nPaste here the path of your folder: (Example: C:%s%sPython3.5;Remember to use %s%s if you are using WINDOWS, but with you are using OS X or LINUX use / instead of %s%s .)\n-> ' % (barra,barra,barra,barra,barra,barra))

listFile = os.listdir(pathFolder)
numberPrefix = 1
namePrefix = input('\nFirst, enter the name of prefix: ')
extensionPrefix = input('\nEnter the file extension: ')

path = input('\nPlease enter again the same path of your folder, but now with just one bar: ')
for num in listFile:
    
    prefix = ((namePrefix)+('%d' % (numberPrefix))+(extensionPrefix))

    if num.endswith(extensionPrefix):
        x = num.find(namePrefix)
        y = num.find(extensionPrefix)
        if (x != -1 and y != -1):
            prefix = ((namePrefix)+('%d' % (numberPrefix))+(extensionPrefix))
            print(num)
            print(prefix)
            os.rename(((path)+('%s' % (barra))+(num)), ((path)+('%s' % (barra))+(prefix)))
            numberPrefix = numberPrefix + 1