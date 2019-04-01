import os
import sys
import getmd5
import hashlib
import json
md5cha={}
md5ch={}
md5noch={}
md5changed={}
json_file="/root/cyber/files.json"
for mydir,subdir,myfile in os.walk('/bin'):
    for myfile in myfile:
        path=os.path.join(mydir,myfile)
        checksum = getmd5.getmd5(path)
        md5cha[path]=checksum
       # json.dump(md5dir,open('files.json','w'),indent=2)
md5ch=json.load(open(json_file))
change="/root/cyber/chaged.txt"
files=open(change,'w')
for i in md5cha.keys():
    for j in md5ch.keys():
        if j==i:
            if md5cha[i] == md5ch[j]:
                md5noch[i]=md5cha[i]
            else:
                md5changed[i]=md5cha[i]

json.dump(md5changed,open('changedfiles.json','w'),indent=2)


