import os,platform,zlib
os.system('termux-setup-storage')
os.system('git pull')
DEVIL=platform.architecture()[0]
 
if DEVIL=="32bit":
 
	
 
	__import__("D3VIL32")
 
elif DEVIL=="64bit":
 
	
 
    __import__("D3VIL")
