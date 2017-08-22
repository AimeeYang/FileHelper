import os.path as opath
import os
import shutil
from stat import ST_MTIME, ST_ATIME, ST_CTIME,ST_SIZE

filesMap={}
ignoreFolderType = [".idea", ".ignore"]
ignoreFileType = [".thumb"] #????????????
directRemoveFileType = [".thumb"]
# TODO logfile split by loginfo, logerror...
# TODO ADD IGNORE LOGIG
def removeDuplicateFile(oriRootDir, tmpDir, logf = None, rules=None, storeDir = None):
    '''
    move dumplicate file to tmpDir.
    :param oriRootDir: 
    :param tmpDir: store duplicate file
    :param logf: maybe {} map, logfiles
    :param rule: maybe[] rule to decide decide leave which one. Option one are 'size', 'lastmodifiedtime', 'lastchangedtime'
    :param storeDir: if not None, then copy none duplicate file to this folder
    :return: 
    '''

    # verify para
    if opath.exists(oriRootDir) and opath.isdir(oriRootDir):
        tmpRootDir = oriRootDir
        for (pathname, dirnames, filenames) in os.walk(tmpRootDir):
            if opath.split(pathname)[1] in ignoreFolderType:
                continue
            for filename in filenames:
                if opath.splitext(filename)[1] in ignoreFileType:
                    continue
                curFullName = os.path.join(pathname, filename)
                # (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
                print(filename + "--", end='')
                print(os.stat(curFullName))
                fileinfo = os.stat(curFullName)
                curfileObj = {
                    "fullname": curFullName,
                    "size": fileinfo[ST_SIZE], # TypeError: tuple indices must be integers or slices, not str
                    "lastaccessed": fileinfo[ST_ATIME],
                    "lastmodified": fileinfo[ST_MTIME],
                    "lastchanged": fileinfo[ST_CTIME],
                    "filecnt": 1
                }
                # unixtime 2017/7/4 15:13:38
                # nlink, uid, gid: no use in windows
                # The size of the file, in bytes.
                # atime: last accessed
                # mtime: last modified
                # ctime: last changed
                if filename in filesMap:
                    filecnt = filesMap[filename]["filecnt"] + 1
                    for rule in rules:
                        if rule == "size":
                            if filesMap[filename]["size"] < fileinfo[ST_SIZE]:
                                removeFile(filesMap[filename]["fullname"], tmpDir, filecnt, logf)
                                filesMap[filename] = curfileObj
                            else:
                                removeFile(curFullName, tmpDir, filecnt, logf)
                            break

                        if rule == "lastmodifiedtime":
                            if filesMap[filename]["lastmodified"] < fileinfo[ST_MTIME]:
                                removeFile(filesMap[filename]["fullname"], tmpDir, filecnt, logf)
                                filesMap[filename] = curfileObj
                            else:
                                removeFile(curFullName, tmpDir, filecnt, logf)
                            break
                        if rule == "lastchangedtime":
                            if filesMap[filename]["lastchanged"] < fileinfo[ST_CTIME]:
                                removeFile(filesMap[filename]["fullname"], tmpDir, filecnt, logf)
                                filesMap[filename] = curfileObj
                            else:
                                removeFile(curFullName, tmpDir, filecnt, logf)
                            break
                    filesMap[filename]["filecnt"] = filecnt
                else:
                    filesMap[filename] = curfileObj


    else:
        logMsg("oriRootDir should be exists and should be a directory", logf)

# def keepRuleBySize(storedOne, current):
#     '''
#     keep file by compare two file's size.
#     :param storedOne: old keep one
#     :param current: current one
#     :return: 1 - keep current; 0 - keep old
#     '''
#
#     return None

def removeFile(src, dst, filecnt,logf):
    curfilename = opath.split(src)[1]
    curdst = dst
    if opath.exists(opath.join(dst, curfilename)):
        curfname, curfext = opath.splitext(curfilename)
        curdst = opath.join(dst, curfname+str(filecnt-1)+curfext)
    shutil.move(src, curdst)
    logMsg("Move ,"+src+", to ,"+curdst, logf)

def logMsg(msg, logf):
    if not (logf is None):
        print(msg, file=logf)
    print(msg)
