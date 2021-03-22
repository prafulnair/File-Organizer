import os 
import shutil
import glob
import os
def Scan():                                           #USING GLOB, SCAN? walk the given directory and list the types eof file, and count .
	c=0
	c1=0
	c2=0
	c3=0
	strpath=eval(input("Enter the path directory"))
	os.chdir(strpath)
	print("the text files are ")
	for file in glob.glob("*.txt"):
		c=c+1
		print(file)
	print("\n the total text files are",c)
	print("********************************************************************************************")
	c=0
	for file in glob.glob("*.mp3"):
		c2=c2+1
		print(" the Music files are ")
		print(file)
	print("\n the total music files are",c2)
	print("********************************************************************************************")
	c=0
	for file in glob.glob("*.lnk"):
		c=c+1
		print(" the shortcuts are",file)
	print("\n The total number of shortcuts are ",c)
	print("********************************************************************************************")
	c=0
	for file in glob.glob("*.docx"):
		c1=c1+1
		print(" the documents are",file)
	
	for file in glob.glob("*.pdf"):
		c1=c1+1
		print(" the documents are",file)
	print("\n the total number of Documents are ",c1)
	print("********************************************************************************************")
	c=0
	for file in glob.glob("*.exe"):
		c=c+1
		print(" the APPLICATIONS  are",file)
	print("\n the total number of APPLICATIONS  are ",c)
	c=0
	print("********************************************************************************************")
	for file in glob.glob("*.mkv") or file in glob.glob("*.mp4"):
		c=c+1
		print(" THE VIDEOS ARE ",file)
	print("\n the total number of VIDEOS are ",c)
	print("********************************************************************************************")
	c=0
	for file in glob.glob("*.png") or file in glob.glob("*.bmp"):
		c=c+1
		print("The IMAGES are ", file)
	print("The total number of images are",c)
	print("********************************************************************************************")
	c=0
	for file in glob.glob("*.c") or file in glob.glob("*.cpp")or file in glob.glob("*.java")or file in glob.glob("*.py"):
		c=c+1
		print("Files with codes are :",file)
	print("The total number of code files are",c)
	print("********************************************************************************************")
	c=0
	
def create():                                      #WE ARE JUST CREATING DIRECTORIES/FOLDER HERE
	str1=eval(input("enter the directory"))
	str2="//Documents"
	str3=str1+str2
	os.makedirs(str3)
	str6="//MUSIC FILES"
	str7=str1+str6
	os.makedirs(str7)
	str8="//IMAGES"
	str9=str1+str8
	os.makedirs(str9)
	str10="//VIDEOS"
	str11=str1+str10
	os.makedirs(str11)
	str12="//SHORTCUTS"
	str13=str1+str12
	os.makedirs(str13)
	str14="//APPLICATIONS"
	str15=str1+str14
	os.makedirs(str15)
	str16="//CODES"
	str17=str1+str16
	os.makedirs(str17)

def Removejunk():
	c=0
	standard = 1000
	import os
	for dirpath, dirs, files in os.walk('.'):
		for file in files: 
			path = os.path.join(dirpath, file)
			if os.stat(path).st_size<=standard:
				c=c+1
				os.remove(path)
	print(" JUNK FILES SUCCESSFULLY REMOVED" )
	print(" Total files removed :",c)

def Organize():
	source=eval(input("Enter the source folder"))
	sourcefiles = os.listdir(source)
	destination=eval(input("Enter the destination"))
	for file in sourcefiles:
		if file.endswith('.png')or file.endswith('.jpg') or file.endswith('.bmp'):
			str1="//IMAGES"
			destin1=destination+str1
			shutil.move(os.path.join(source,file), os.path.join(destin1,file))
	
	for file in sourcefiles:
		if file.endswith('.docx')or file.endswith('.pdf')or file.endswith('.xml') or file.endswith('.txt')or file.endswith('.ppt')or file.endswith('.rtf'):
			str2="//Documents"
			destin2=destination+str2
			shutil.move(os.path.join(source,file), os.path.join(destin2,file))
	
	for file in sourcefiles:
		if file.endswith('.mp3'):
			str4="//MUSIC FILES"
			destin4=destination+str4
			shutil.move(os.path.join(source,file), os.path.join(destin4,file))
	for file in sourcefiles:
		if file.endswith('.exe'):
			str5="//APPLICATIONS"
			destin5=destination+str5
			shutil.move(os.path.join(source,file), os.path.join(destin5,file))
	for file in sourcefiles:
		if file.endswith('.lnk'):
			str6="//SHORTCUTS"
			destin6=destination+str6
			shutil.move(os.path.join(source,file), os.path.join(destin6,file))
	for file in sourcefiles:
		if file.endswith('.mp4')or file.endswith('.3gp')or file.endswith('.flv')or file.endswith('.mkv'):
			str7="//VIDEOS"
			destin7=destination+str7
			shutil.move(os.path.join(source,file), os.path.join(destin7,file))
	for file in sourcefiles:
		if file.endswith('.c')or file.endswith('.cpp')or file.endswith('.java')or file.endswith('.py')or file.endswith('.pl')or file.endswith('.class'):
			str8="//CODES"
			destin8=destination+str8
			shutil.move(os.path.join(source,file), os.path.join(destin8,file))

def main():
		
		choice=1
		while(choice!=0):
			print("\n 1. SCAN THE DIRECTORY \n 2.CREATE FOLDERS \n 3. Organize \n 4.REMOVE JUNKFILES")
			print(" PLEASE ENTER YOUR CHOICE")
			choice=eval(input())
			if(choice==1):
				Scan()      #we would make a menu driven program choosing to scan or create folder , and organize(move files to folder)
			elif(choice==2):
				create()
			elif(choice==3):
				Organize()
			elif(choice==4):
				Removejunk()
			else:
				exit()
		
main()
