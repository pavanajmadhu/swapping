file1=input("enter you first file's name ")
data_a=open(file1,"r")

file2=input("enter you second file's name ")
data_b=open(file2,"r")

def swapping():
    with open(file1,"w") as a:
     a.write(data_b)
    
    with open(file2,"w") as b:
     b.write(data_a)

swapping()
