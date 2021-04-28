
n = eval(input())
import os
if os.path.exists('files'):
    os.chdir('files')
    for i in os.listdir():
        os.rmdir(i)
    os.chdir('../')
    os.rmdir('files')
os.mkdir("files")
os.chdir("files")
for i in range(1,n+1):
    os.mkdir("f"+str(i))
c = os.listdir()
c.sort()
print(c)

os.rename("f1","folder1")
a = os.listdir()
a.sort()
print(a)

os.rmdir("folder1")
b = os.listdir()
b.sort()
print(b)

for i in os.listdir():
    os.rmdir(i)
os.chdir('../')
os.rmdir('files')


