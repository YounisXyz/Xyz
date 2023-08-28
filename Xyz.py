import os,platform
os.system('git pull')
 
xyz=platform.architecture()[0]
if xyz=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif xyz=="64bit":
    __import__("Xyz")
 
