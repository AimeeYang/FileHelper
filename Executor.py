import MergeFolderHelper.Merger as merger
import os




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
    oriRootDir = 'E:/0-a/ml2'
    outRootDir = './output'
    classificationType = 'fileType'
    logfileName = './log.txt'

    merger.merge(oriRootDir, outRootDir, classificationType, logfileName)