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
        ".xml": "ignore",
    }.get(fileExtension, 'other')

ignoreFolderType = [".idea", ".ignore"]

def merge(oriRootDir, outRootDir, classficationBy, logf = None, recursiveDir = None ):
    '''
    classify all files in oriRootDir by classficationBy, store
    result in outRootDir
    :param oriRootDir:  root directory of files
    :param outRootDir:  results are stored to outRootDir
    :param classficationBy: str, classify by classficationBy, option values: 'fileType' 
    :param logfileName: log file path
    :return: 
    '''

    # if logf is None:
    #     logf = open(logfileName, 'x')
    # Verify para
    if recursiveDir is None:
        recursiveDir = oriRootDir
    if os.path.exists(oriRootDir) and os.path.isdir(oriRootDir):
        if not os.path.exists(outRootDir):
            os.makedirs(outRootDir)
        # dirpaths + dirname/ dirpaths + filename => absolute path
        for (dirpath, dirnames, filenames) in os.walk(recursiveDir):
            if os.path.split(dirpath)[1] in ignoreFolderType:
                continue
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
                if folderType == "ignore":
                    continue
                print("folderType: " + folderType)
                # TODO check if need rename with folder info, like month.. shutil
                # folderDir = os.path.join(outRootDir, os.path.split(recursiveDir)[1], folderType, filename)
                folderDir = os.path.join(os.path.abspath(outRootDir), os.path.split(oriRootDir)[1], folderType) #, filename)
                if not os.path.exists(folderDir):
                    os.makedirs(folderDir)
                dstFileName = shutil.copy(os.path.join(dirpath,filename), folderDir)
                print("copy, " + os.path.join(dirpath,filename)+" , to, "+ dstFileName, file=logf)
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
            # # 注 下面不需要 for (dirpath, dirnames, filenames) in os.walk(recursiveDir) 已包括下面逻辑
            # for dirname in dirnames:
            #     merge(oriRootDir, outRootDir, classficationBy, logf, os.path.join(dirpath, dirname), )
            #     print("Dirname: "+ dirname)
            #     info2 = os.stat(os.path.join(dirpath, dirname))
            #     print("Dirname-info: ", end='')
            #     print(info2)
    else:
        print("ParameterError: oriRootDir should exist and should be a directory")
        print("ParameterError: oriRootDir should exist and should be a directory", file=logf)
    # logf.close()

def getFilesByType(oriRootDir, fileType):
    '''
    use glob get all *.type in a dir, by some trick of regex
    :param oriRootDir: 
    :param fileType: '.txt',...
    :return: file path of the specify type - fileType
    '''

# TODO ADD ignore file type and folder type logic
def verify(oriRootDir, outRootDir, logf = None):
    '''
    check after special operation, no file missing. (By file counts)
    :param oriRootDir: 
    :param outRootDir: 
    :return: True - no file missing; 
              False - some missing 
            
    '''
    # TODO whether give missing info.
    tmpOutDir = os.path.join(os.path.abspath(outRootDir), os.path.split(oriRootDir)[1])
    oriCnt = fileCount(oriRootDir)
    print("============out==============")
    outCnt = fileCount(tmpOutDir)
    if logf is not None:
        print("source file count: "+str(oriCnt)+", out file count: "+ str(outCnt), file=logf)
    print("source file count: " + str(oriCnt) + ", out file count: " + str(outCnt))
    print("verify result: ", end='')
    print(oriCnt == outCnt)
    print("verify result: " + str(oriCnt == outCnt), file=logf)
    return oriCnt == outCnt

# FIND DOUBLE REASON
# # 注 下面不需要 for (dirpath, dirnames, filenames) in os.walk(recursiveDir) 已包括下面逻辑
# for dirname in dirnames:
# TODO ADD ignore file type and folder type logic
def fileCount(dir):
    fileCnt = 0
    for dirpath, dirnames, filenames in os.walk(dir):
        if os.path.split(dirpath)[1] in ignoreFolderType:
            continue
        fileCnt += len(filenames)
        # # 注 下面不需要 for (dirpath, dirnames, filenames) in os.walk(recursiveDir) 已包括下面逻辑
        # for dirname in dirnames:
        #     fileCnt += fileCount(os.path.join(os.path.abspath(dirpath), dirname))
    print(dir + " file cnt: "+ str(fileCnt))
    return fileCnt