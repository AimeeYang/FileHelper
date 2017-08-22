
import os
from os.path import splitext, exists, isdir,split
from shutil import copy
import Utils.Common as common
import random
import re
import glob

def renameWithFixPrefixAndDateInfo(oriRootDir, outDir, fixedPrefix, regexStr, fileType = None, logf = None):
    '''
    return file name like fixedPrefix+dateinfo(from ori filename)
    :param oriRootDir: source root directory
    :param outDir: result store directory
    :param fixedPrefix: 
    :param regexStr: r'\d+'
    :param fileType: '.mp3'
    :param logf: 
    :return: 
    '''
    # para verify
    if not (exists(oriRootDir) and isdir(oriRootDir)):
        msg = "oriRootDir should be exists and should be oriRootDir"
        common.printLog(msg, logf)
    if not (exists(outDir)):
        os.makedirs(outDir)

    for (path, dirs, files) in os.walk(oriRootDir):
        for filename in files:
            parts = splitext(filename)
            if parts[1] != fileType:
                continue
            dateInfos = re.findall(regexStr, parts[0])
            dateInfos = [tmpinfo for tmpinfo in dateInfos if len(tmpinfo)==4]
            keepOriname = False
            if len(dateInfos) == 0 or len(dateInfos) > 1:
                common.printLog("Oops! special name! "+ os.path.join(path, filename))
                keepOriname = True
            dateInfo = ''.join(dateInfos)
            newName = fixedPrefix + dateInfo + parts[1]
            if keepOriname:
                newName = 'ori_'+split(path)[-1]+"_"+filename
            while exists(os.path.join(outDir, newName)):
                # path rand => then man deal with duplicate one
                randnum = random.randint(0, 100)
                newName = fixedPrefix + dateInfo + randnum +  parts[1]
            common.printLog("current file: " + os.path.join(path, filename))
            common.printLog("move to : "+os.path.join(outDir, newName))
            copy(os.path.join(path, filename), os.path.join(outDir, newName))

def verify(oriDir, outDir, fileType):
    filePattern = "**\\*"+fileType
    return len(glob.glob(os.path.join(oriDir+'\\'+"**\\*"+fileType), recursive=True)) - \
           len(glob.glob(os.path.join(outDir + '\\' + "**\\*" + fileType), recursive=True))