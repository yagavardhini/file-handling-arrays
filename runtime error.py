a=[1,2,3]
try:
    print("sec element:%d"%(a[1]))
    print("fourth element:%d"%(a[3]))
except IndexError:
    print("an error occured")
