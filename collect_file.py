import glob
import os
from shutil import copy

def collect_file(srcDir, tarDir, fileType):
    if not os.path.exists(tarDir):
        os.makedirs(tarDir)
    for fname in glob.glob(os.path.join(srcDir+'\\'+"**\\*"+fileType), recursive=True):
        ffdir, ffname = os.path.split(fname)
        new_path = os.path.join(tarDir,ffname)
        num = 1
        while os.path.exists(new_path):
            fn,fex = os.path.splitext(ffname)
            new_ffname = "{}_{}{}".format(fn,str(num),fex)
            new_path = os.path.join(tarDir,new_ffname)
            num = num + 1
        print("src: {}".format(fname))
        print("tar: {}".format(new_path))
        copy(fname, new_path)


