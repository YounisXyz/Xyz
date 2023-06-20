import os,platform
os.system('git pull')
 
Xyz=platform.architecture()[0]
if Xyz=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif Xyz=="64bit":
    __import__("xyz")
 
