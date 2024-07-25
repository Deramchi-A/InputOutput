import os
size=os.stat('test.txt').st_size
print(size)
if size==0:
    print('the file is empty')
else:
    print('the file is not empty')