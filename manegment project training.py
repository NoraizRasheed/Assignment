
print("welcome to school management system")
print("for enter a new student press + :\nfor check record of a student press r :\n")

opp=input("enter your desired operator:\n")
if (opp=="+"):
    add_std()    
    #father_name()
elif opp=="r":
    #print("enter a student name:\n")
    #search_name=std_list
    
    '''search_name=list(std_list)
    x=input(print("enter a student name to find:\n"))

    search_name.append(x)
    if(x in search_name):
        print("student record is :\n",add_std())
    else:'''
    #print("no records found")
    
    std_record()
    


def add_std():
    
    #std_list = [x.strip() str(input("enter student name separated by , :")).split(',')]
    std_list=[]
    father_list=[]
    cnic_list=[]
    phone_num=[]
    std=str(input("enter student name:\n"))
    father=str(input("enter father name:\n"))
    cnic=str(input("enter your cnic number:\n"))
    cell_num=str(input("enter your cell number:\n"))
    std_list.append(std)
    father_list.append(father)
    cnic_list.append(cnic)
    phone_num.append(cell_num)
    print("student name:",std_list)
    print("\nfather name :",father_list)
    print("\ncnic:",cnic_list)
    print("\nphone number:",phone_num)
    print("new student record added.\n")
    new_record=list(std_list+father_list+cnic_list+phone_num)
    print(new_record)
    #print("enter n to enter a new record or x to close:\n")
    #opp1=str(input(""))
    #if opp1=="n":
        #add_std()
    #else:
        #exit()
    

def std_record():
    stu_list=["noraiz","osama","usman","ahmad"]
    this_list=list(stu_list)
    #search_name=[]
    x=input(print("enter a student name to find:\n"))

    if x in this_list:
        print("student record is :\n")
        print(x)
    else:
        print("no records found")