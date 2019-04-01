import os
import sys
import getmd5
import hashlib
import json
md5dir={}
perm={}
for mydir,subdir,myfile in os.walk('/bin'):
    for myfile in myfile:
        path=os.path.join(mydir,myfile)
        checksum = getmd5.getmd5(path)
        md5dir[path]=checksum
        info = os.stat(path)
        per=oct(info.st_mode)[-3:]
        perm[path]=per

        json.dump(md5dir,open('files.json','w'),indent=2)
        json.dump(perm,open('permission.json','w'),indent=2)


