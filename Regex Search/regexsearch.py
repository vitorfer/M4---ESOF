import os
barra = '\\'
print('FIRST YOU NEED CREAT SOME .txt FILES OR SELECT A FOLDER THAT ALREADY EXIST WHAT YOU WANT TO FIND!\n\n')
pathFile = input('Paste here the path of your folder: (Example: C:%s%sPython3.5; Remember to use %s%s if you are using WINDOWS but if you are using OS X or LINUX use / instead of %s%s .)\n->' % (barra,barra,barra,barra,barra,barra))
listFile = os.listdir(pathFile)

expressionFiles = input('Enter with your expression that you want to find de file:\n->')
print('\n')
for numb in listFile:
    tamanho = (len(numb))
    if numb[(tamanho - 4):] == '.txt':
      phraseFile = open(pathFile+barra+barra+numb)
      listphrase = phraseFile.readlines()
      for numb1 in listphrase:
          taman1 = len(expressionFiles)
          taman2 = len(numb1)
          answerFile = (expressionFiles in numb1)
          if answerFile == True:
              print ('The expression %s is in %s file.' % (numb1, numb))    
