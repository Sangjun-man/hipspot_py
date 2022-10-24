import os
import json

rootPath = ('./src/images')


f_images = os.listdir(rootPath)

for dir in f_images:
    if dir[0:1] == '@':
        dirPath = rootPath + '/' + dir

        clientSrcPath = ('/images'+'/' + dir)

        saveFilePath = './data'
        menuDir = os.path.expanduser(dirPath + '/menu')
        storeDir = os.path.expanduser(dirPath + '/store')
        storeList = os.listdir(storeDir)
        menuList = os.listdir(menuDir)

        storeSrcList = []
        menuSrcList = []

        for fileName in storeList:
            storeSrcList.append(
                {'src': clientSrcPath + '/store' + '/' + fileName})
        for fileName in menuList:
            menuSrcList.append(
                {'src': clientSrcPath + '/menu' + '/' + fileName})

        fileDict = {
            'instaId': dir,
            "data": [
                {
                    'type': "storeImage",
                    "name": "업체제공사진",
                    'imageList': storeSrcList,
                },
                {
                    "type": 'menuImage',
                    'imageList': menuSrcList,
                    "name": "메뉴"
                }
            ]
        }

        # print(dirPath, json.dumps(fileDict, indent=4))

        jsonString = json.dumps(fileDict, ensure_ascii=False, indent="\t")
        if not os.path.exists(saveFilePath):
            os.makedirs(saveFilePath)
        jsonFile = open(saveFilePath + '/' + dir +
                        '.json', 'w', encoding='utf-8')
        jsonFile.write(jsonString)
        jsonFile.close()
