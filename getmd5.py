import hashlib

def getmd5(f):
  
  md5obj = hashlib.md5()
  SIZE = 1024 * 1000
  
  with open(f,'rb') as fh:
    while True:
      data = fh.read(SIZE)
      if data:
        md5obj.update(data)
      else:
        break
  return md5obj.hexdigest() 
