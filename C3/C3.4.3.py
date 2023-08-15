import os

def check_dir():
    my_dir = os.getcwd()
    return os.walk(my_dir,True,)

check_dir()

for i,b,c in os.walk(os.getcwd()):
    print ('\n', i,'\n', b,'\n', c)
    # print(i)
