#my solution
new_file=open('new_file.txt','x')
lines=open("test.txt", 'r')
list_lines=[]
for i in lines:
    if "5"not in i:
        list_lines.append(i)
write=open('new_file.txt','w')
write.writelines(list_lines)
    
print(list_lines)
'''
#the best solution
# read test.txt
with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()

# open new file in write mode
with open("new_file.txt", "w") as fp:
    count = 0
    # iterate each lines from a test.txt
    for line in lines:
        # skip 5th lines
        if count == 4:
            count += 1
            continue
        else:
            # write current line
            fp.write(line)
        # in each iteration reduce the count
        count += 1
'''