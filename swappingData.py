file1=input("enter you first file's name ")
with open(file1,"r") as a:
    data_a=a.read()

file2=input("enter you second file's name ")
with open(file2,"r") as b:
    data_b=b.read()
    
def swapping():
    with open(file1,"w") as a:
     a.write(data_b)
    
    with open(file2,"w") as b:
     b.write(data_a)

swapping()
