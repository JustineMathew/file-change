import os
import sys
import getmd5
import hashlib
import json
md5dir={}
perm={}
for curdir,subdir,curfile in os.walk('/bin'):
    for curfile in curfile:
        path=os.path.join(curdir,curfile)
        checksum = getmd5.getmd5(path)
        md5dir[path]=checksum
        info = os.stat(path)
        per=oct(info.st_mode)[-3:]
        perm[path]=per
        md5dir[path]=[checksum,per]
        json.dump(md5dir,open('files.json','w'),indent=2)


