import os,re,sys,platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    from YounisXyz import XYZ
    XYZ()
elif bit == '32bit':
    exit('\033[1;91mSorry This Tools Not Working on 32 Bit Device')
 
 
