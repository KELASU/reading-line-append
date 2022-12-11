readingfile = open ("textfile.txt","r")

def method1 (readingfile):
    method11 = readingfile.read()
    method12 = method11.splitlines()
    return method12

def method2(readingfile):
    method21 = readingfile.readlines()
    return method21


method1s = method1(readingfile)
readingfile.seek(0)
method2s = method2(readingfile)
readingfile.seek(0)


print(method1s)
print(method2s)
