with open("test.txt", 'r') as fp:
    # lines to read
    line_numbers = [4,1, 7]
    # To store lines
    lines = []
    for i, line in enumerate(fp):
        print(i,line)
        # read line 4 and 7
        if i in line_numbers:
            lines.append(line.strip())
        elif i > 7:
            # don't read after line 7 to save time
            break
print(lines)

'''
#The best solution
# read file
with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()
    # get line number 3
    print(lines[2])

'''