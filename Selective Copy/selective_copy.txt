import shutil, os

barra = '\\'
print('FIRST YOU NEED TO SEARCH THE PATH OF THE FOLDER THAT YOU WANT TO COPY FILES WITH .pdf OR .jpg')

pathFolder = input('\nPaste here the path of your folder: (Example: C:%s%sPython3.5;Remember to use %s%s if you are using WINDOWS, but with you are using OS X or LINUX use / instead of %s%s .)\n-> ' % (barra,barra,barra,barra,barra,barra))
listFile = os.listdir(pathFolder)

newDestination = input('\n\nNow, please, paste here the path of the destination that you want for the files in this folder: (Read the previous tips about path!)\n-> ')
for num in listFile:
    if num.endswith('.pdf') or num.endswith('.jpg'):
        print (('\nThis file will be copy to the path that you put: ')+(pathFolder)+('%s%s'%(barra,barra))+(num))
        shutil.copy(((pathFolder)+('%s%s'%(barra,barra))+(num)), newDestination)