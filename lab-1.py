def add(a,b):
    print(a+b)
    
add(3,4)  

def student(name,rollno,clas="sy"):
    print(name,rollno,clas)
    
student("krutik",27,)    

def student2(name,rollno):
    print(name,rollno)
    
student2(rollno=23,name="yash")  

def subject3(*subjects):
    print(subjects)
   
subject3("math","science","chemistry")    

my_list=[]
n=3
for i in range(n):
    sub=input("enter your subjects:")
    my_list.append(sub)
    
subject3(my_list)    
    
    