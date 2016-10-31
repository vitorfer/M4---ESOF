import shutil, os

barra = '\\'
print('FIRST YOU NEED TO SEARCH THE PATH OF THE FOLDER THAT YOU WANT TO COPY FILES WITH .pdf OR .jpg')
pathFolder = input('\nPaste here the path of your folder: (Example: C:%s%sPython3.5;Remember to use %s%s if you are using WINDOWS, but with you are using OS X or LINUX use / instead of %s%s .)\n-> ' % (barra,barra,barra,barra,barra,barra))
listFile = os.listdir(pathFolder)

for num in listFile:
    pathSize = ((pathFolder)+('%s%s' % (barra,barra))+(num)) 
    fileSize = os.path.getsize(pathSize)
    if (fileSize > 100000000):
       print ((pathFolder)+('%s%s' % (barra,barra))+(num))