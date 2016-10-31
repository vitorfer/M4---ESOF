import zipfile, os 

def backupToZip(folder):

    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    backupToZip('C:\\delicious')

    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break;
        number = number + 1

    print('Creating %s..' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

backupToZip('C:\\delicious')
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backupZip.write(foldername)
        for filename in filenames:
            newBase / os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupzip.write(os.path.join(foldername,filename))
    backupZip.close()
    print('Done.')