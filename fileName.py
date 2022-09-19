import os
import unicodedata

src = ('/Desktop/coding/hipspot/public/images')

file_to_open = os.path.expanduser('~' + src)
# f = open(file_to_open)
f_images = os.listdir(file_to_open)
# print(f_images)


def toNFCnomalizeStr(str):
    return unicodedata.normalize('NFC', str)


def delExtenstion(str):
    return str[0:str.index('.')]


for dir in f_images:
    if dir[0:1] == '@':
        dirPath = '~' + src + '/' + dir
        menuDir = os.path.expanduser(dirPath + '/menu')
        storeDir = os.path.expanduser(dirPath + '/store')
        print(os.listdir(menuDir), os.listdir(storeDir))

        for file in os.listdir(storeDir):
            extension = file[file.index('.'): len(file)]
            fileName = toNFCnomalizeStr(delExtenstion(file))
            filePathName = os.path.expanduser(storeDir + '/' + file)

            if fileName == '일':
                # print(file)
                os.rename(filePathName, os.path.expanduser(
                    storeDir + '/' + '0' + extension))
            elif fileName == '이':
                os.rename(filePathName,  os.path.expanduser(
                    storeDir + '/' + '1' + extension))
            elif fileName == '삼':
                os.rename(filePathName,  os.path.expanduser(
                    storeDir + '/' + '2' + extension))
            elif fileName == '사':
                os.rename(filePathName,  os.path.expanduser(
                    storeDir + '/' + '3' + extension))
            elif fileName == '오':
                os.rename(filePathName,  os.path.expanduser(
                    storeDir + '/' + '4' + extension))

        for index, file in enumerate(os.listdir(menuDir)):
            if file[len(file)-1: len(file)] != 'g':
                extension = '.png'
            else:
                extension = file[file.index('.'): len(file)]

            filePathName = os.path.expanduser(menuDir + '/' + file)
            # print('for문속file',  file, filePathName, menuDir)
            if len(file) > 1:
                os.rename(filePathName, os.path.expanduser(
                    menuDir + '/' + str(index) + '.png'))
            os.rename(filePathName, os.path.expanduser(
                menuDir + '/' + str(index) + extension))
