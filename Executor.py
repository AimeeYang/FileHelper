import MergeFolderHelper.Merger as merger
import DuplicateFileHelper.Remover as remover
import Proprecessing.Rename as rename
import os
import re




if __name__ == "__main__":
    # oriRootDir = input("Please enter 'oriRootDir' as source root directory: ")
    # while (not os.path.exists(oriRootDir)) or (not os.path.isdir(oriRootDir)):
    #     print("oriRootDir should be exist and should be directory")
    #     oriRootDir = input("Please enter 'oriRootDir' as source root directory: ")
    #
    # outRootDir = input("Please enter 'outRootDir' to store result: ")
    # classificationType = input("Please enter 'classificationType', option value are fileType, : ")
    # while merger.ClassificationType.index(classificationType) < 0:
    #     print("classificationType should be in ", end='')
    #     print(merger.ClassificationType)
    #     classificationType = input("Please enter 'classificationType', option value are fileType, : ")
    #
    # logfileName = input("Please enter 'logfileName' to store log: ")
    # while os.path.exists(logfileName):
    #     print("logfileName should not be exist.")
    #     logfileName = input("Please enter 'logfileName' to store log: ")

    # for test
    # oriRootDir = 'E:/0-tmp'
    # outRootDir = './output'
    # classificationType = 'fileType'
    # logfileName = './log_remove.txt'
    #
    # rules=['size', 'lastmodifiedtime', 'lastchangedtime']
    # remove then merge
    # TODO SOME OPTIMIZE
    # logf = open(logfileName, 'x')


    # remover.removeDuplicateFile(oriRootDir,outRootDir, None, rules)
    # merger.merge(oriRootDir, outRootDir, classificationType, logf)
    # merger.verify(oriRootDir, outRootDir, logf)
    # logf.close()


    # tmpOutDir = os.path.join(os.path.abspath(outRootDir), os.path.split(oriRootDir)[1])
    # merger.fileCount(tmpOutDir)
    # cnt = 0
    # ## 注意下面的循环次数 为所有folder个数 rootfolder + subfolder 个数
    # for dirpath, dirnames, filenames in os.walk(tmpOutDir):
    #     cnt += 1
    #     print("dirpath: " +dirpath)
    #     print("dirnames: ")
    #     print(dirnames)
    #     print("filenames:")
    #     print(filenames)
    #     print(str(cnt))

    # Rename
    oriRootDir = 'D:\\dir'
    outDir = 'E:/0-tmp_1/'
    fixedPrefix = 'xzf'
    regexStr = r'\d+'
    fileType = '.mp3'
    rename.renameWithFixPrefixAndDateInfo(oriRootDir, outDir, fixedPrefix, regexStr, fileType, None)
    print("verify result: "+ str(rename.verify(oriRootDir, outDir, fileType)))
    print("End Rname")