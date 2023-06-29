import os,platform
os.system('git pull')
 
Xyz=platform.architecture()[0]
if Xyz=="32bit":
    __import__("Xyz32")
elif Xyz=="64bit":
    __import__("Xyz")
 
