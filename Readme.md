
1-Create a file:
with open ("test.txt",'w') as fp:
    fp.write('new line')

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist
2-Read a file:
with open ("test.txt",'r') as fp:
    fp.read()
3-Rename and remove a file :
 os.rename('old name','new name')
 os.remove('file path')
4-Copy and move a file:
 shutil.copy('src file path','new path')
 shutil.move('src file path','new path')
5-Working with directories:
 os.listdir('dir path') #Get all files.
 shutil.rmtree('dir path')
 shutil.copytree('src path','dist path') #copy dir
