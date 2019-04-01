import os
import sys
import getmd5
import hashlib
import json

#Dictinory to store old values
md5old={}

#Dictinory to store new values
md5new={}

#Dictinary which shows file has not changed
md5nochange={}

#Dictinary which shows files have changed
md5changed={}

out='No changes in the files'
json_file="/root/cyber/files.json"

#Takes the file checksum
for curdir,subdir,curfile in os.walk('/bin'):
    for curfile in curfile:
        path=os.path.join(curdir,curfile)
        checksum = getmd5.getmd5(path)
        info = os.stat(path)
        per=oct(info.st_mode)[-3:]
        md5new[path]=[checksum,per]
       # json.dump(md5dir,open('files.json','w'),indent=2)
md5old=json.load(open(json_file))
change="/root/cyber/chaged.txt"
files=open(change,'w')

#compairing the values
for oldkey,oldvalue in md5old.items():
    oldv1,oldv2=oldvalue
    for newkey,newvalue in md5new.items():
        newv1,newv2=newvalue
        if oldkey==newkey:
            if oldv1!=newv1: 
                out="This  contents are changed"
                md5changed[oldkey]=out
            if oldv2!=newv2:
                out="This  permissions are changed"
                md5changed[oldkey]=out
            if oldv1!=newv1 and oldv2!=newv2:
                out="This files permissios and contents are changed"
                md5changed[oldkey]=out
           # if oldv1!=newv1 and oldv2==newv2:
            #    out="This files contents are changed"
   # md5changed[oldkey]=out

json.dump(md5changed,open('changedfiles.json','w'),indent=2)


