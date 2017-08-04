import os
import glob
import shutil


# Refer: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory

# TODO use glob get all *.type in a dir, by some trick of regex

# TODO use os.listdir, os.walk, can do some modify to file.

# Refer: https://stackoverflow.com/questions/10937350/how-to-check-type-of-files-without-extensions-in-python
#   can get file type from file content, and without use of file extension information

ClassificationType = ['fileType']

def fileTypeConverter(fileExtension):
    # here according dict values classify file
    return {
        ".pdf": "pdf",
        ".jpg": "img",
        ".jpeg": "img",
        ".png": "img",
        ".rar": "zip",
        ".zip": "zip",
        ".mp3": "mp3",
        ".mp4": "video",
    }.get(fileExtension, 'other')

def merge(oriRootDir, outRootDir, classficationBy, logfileName):
    '''
    classify all files in oriRootDir by classficationBy, store
    result in outRootDir
    :param oriRootDir:  root directory of files
    :param outRootDir:  results are stored to outRootDir
    :param classficationBy: str, classify by classficationBy, option values: 'fileType' 
    :param logfileName: log file path
    :return: 
    '''

    logf = open(logfileName, 'x')
    # Verify para
    if os.path.exists(oriRootDir) and os.path.isdir(oriRootDir):
        if not os.path.exists(outRootDir):
            os.makedirs(outRootDir)
        # dirpaths + dirname/ dirpaths + filename => absolute path
        for (dirpath, dirnames, filenames) in os.walk(oriRootDir):
            for filename in filenames:
                # test
                # fullFileName = os.path.join(dirpath, filename)
                # fname, fext = os.path.splitext(fullFileName)
                # print('fname: '+fname)
                # print('fext: '+fext)
                fname, fext = os.path.splitext(filename)
                print('fname: ' + fname)
                print('fext: ' + fext)
                folderType = fileTypeConverter(fext)
                print("folderType: " + folderType)
                # TODO check if need rename with foler info, like month.. shutil
                # folderDir =
            # # logf.write("")
            # for filename in filenames:
            #     print("File: "+filename)
            #     info = os.stat(os.path.join(dirpath, filename))
            #     print("File-info: ",end='')
            #     print(info)
            # # for dirpath in dirpaths:
            # #     print("Path: "+dirpath)
            # print("Path: ", end='')
            # print(dirpath)
            # for dirname in dirnames:
            #     print("Dirname: "+ dirname)
            #     info2 = os.stat(os.path.join(dirpath, dirname))
            #     print("Dirname-info: ", end='')
            #     print(info2)
    else:
        print("ParameterError: oriRootDir should exist and should be a directory")
        print("ParameterError: oriRootDir should exist and should be a directory", file=logf)
    logf.close()

def getFilesByType(oriRootDir, fileType):
    '''
    use glob get all *.type in a dir, by some trick of regex
    :param oriRootDir: 
    :param fileType: '.txt',...
    :return: file path of the specify type - fileType
    '''


def verify(oriRootDir, outRootDir):
    '''
    check after special operation, no file missing. (By file counts)
    :param oriRootDir: 
    :param outRootDir: 
    :return: True - no file missing; 
              False - some missing 
            
    '''
    # TODO whether give missing info.