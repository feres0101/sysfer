#!/usr/bin/env python3
# -*- codign: utf-8 -*-

''' 
                __                         
 ___ _   _ ___ / _| ___ _ __   _ __  _   _ 
/ __| | | / __| |_ / _ \ '__| | '_ \| | | |
\__ \ |_| \__ \  _|  __/ |    | |_) | |_| |
|___/\__, |___/_|  \___|_|    | .__/ \__, |
     |___/                    |_|    |___/ 
                                              

%^| BY **https://www.github.com/feres0101**

'''


from shutil import rmtree
from os import remove,removedirs

def Elimina(x):
	''' x = Path File/Dir Remove Python'''
	
	try:
		
		try:
			removedirs(x)
		
		except:
		
			try:
				rmtree(x)
		
			except:
				remove(x)

	except:
		print("Errore File non essistente")

if __name__ == "__main__":
	x = str(input("Path Dir/File Remove = "))
	Elimina(x)
