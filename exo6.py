
# writing new content to the file
for i in range (6):
    i=str(i)
    text = "This is new content \n" + i
    fp = open("test.txt ", 'a')
    fp.write(text)
    print('Done Writing')
fp.close()

# Open the file for reading the new contents
fp = open("test.txt", 'r')
print(fp.read())
fp.close()
