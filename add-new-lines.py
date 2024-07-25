
# writing new content to the file
open ('test.txt',"x")
for i in range (6):
    i=str(i)
    text = "This is new content " + i + '\n'
    fp = open("test.txt ", 'a')
    fp.writelines(text)
    print('Done Writing')
    fp.close()

# Open the file for reading the new contents
print(open("test.txt", 'r'))


