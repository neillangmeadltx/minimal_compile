import os
import subprocess
import re

def get_filename():
    #filename = "OPCO_OperationControl.c"
    #filename = "ANIO_AnalogInOutFunctions.c"
    filename = "test_1.c"
    return filename

def delete_inc():
    cmd = "del /s /q inc"
    print("Deleting inc directory...")
    stdoutdata = subprocess.getoutput(cmd)

def create_inc():
    cmd = "mkdir inc"
    print("Creating inc directory...")
    stdoutdata = subprocess.getoutput(cmd)

def process_include_stmt(line):
    #print ("Processing line" , line)
    #re.IGNORECASE

    d0_a = re.search("^#include \"([a-zA-Z0-9_]*.h)\"$", line) # single nested #include in quotes"
    d0_b = re.search("^#include <([a-zA-Z0-9_]*.h)\>$", line)  # single nested #include in < >
    
    d1_a = re.search("^#include \"([a-z0-9]*)/([a-zA-Z0-9_]*.h)\"$", line) # one directory deep, "quotes"
    d1_b =re.search("^#include <([a-z0-9]*)/([a-zA-Z0-9_]*.h)>$", line) # one directory deep, < >

    d2_a = re.search("^#include \"([a-z0-9]*)/([a-z0-9]*)/([a-zA-Z0-9_]*.h)\"$", line) # two directories deep, "quotes"
    d2_b =re.search("^#include <([a-z0-9]*)/([a-z0-9]*)/([a-zA-Z0-9_]*.h)>$", line) # two directories deep, < >

    d3_a = re.search("^#include \"([a-z0-9]*)/([a-z0-9]*)/([a-z0-9]*)/([a-zA-Z0-9_]*.h)\"$", line) # three directories deep, "quotes"
    d3_b = re.search("^#include <([a-z0-9]*)/([a-z0-9]*)/([a-z0-9]*)/([a-zA-Z0-9_]*.h)>$", line) # three directories deep, < >

    d4_a = re.search("^#include \"([a-z0-9]*)/([a-z0-9]*)/([a-z0-9]*)/([a-z0-9]*)/([a-zA-Z0-9]*.h)\"$", line)
    d4_b = re.search("^#include <([a-z0-9]*)/([a-z0-9]*)/([a-z0-9]*)/([a-z0-9]*)/([a-zA-Z0-9]*.h)>$", line)

    if (d0_a):
        #print ("matched single \"include\" in ", line)
        cmd = "touch " + d0_a.group(1)
        print ("creating include file  " , d0_a.group(1))
        os.system(cmd)
        return
    
    if (d0_b):
        #print ("matched single <include> in ", d1.group(1))
        file = "inc/" + d0_b.group(1)
        cmd = "touch " + file
        print ("creating include file  " , file)
        os.system(cmd)
        return

    if (d1_b):
        directory = "inc\\" + d1_b.group(1)
        print ("directory is ", directory)
        cmd = "mkdir " + directory
        #print (cmd)
        #print (d1_b.group(2))
        filen = directory + "\\" + d1_b.group(2)
        print (filen)
        #cmd = "touch " + file
        # print ("creating include file  " , file)
        os.system(cmd)
        cmd2 = "touch " + filen
        print ("cmd2: ", cmd2)
        os.system(cmd2)
        return 

    if (d2_b):
        print ("Matching two levels", line)
        print (d2_b.group(1))
        print (d2_b.group(2))
        #dir_mk = 
        print (d2_b.group(3))
        cmd1 = "mkdir " + "inc\\" + d2_b.group(1);
        cmd2 = "mkdir " + "inc\\" + d2_b.group(1) + "\\" + d2_b.group(2)
        cmd3 = "touch " + "inc\\" + d2_b.group(1) + "\\" + d2_b.group(2) + "\\" + d2_b.group(3)

        print (cmd1, cmd2, cmd3)
        os.system(cmd1)
        os.system(cmd2)
        os.system(cmd3)
        #os.system()
        return
    
    if (d3_b):
        print ("matching three levels",line)
        return 

    if (d4_b):
        print ("matching four levels",line)
        #print (line)
        #print ("matched 4!")
        dir1 = d4_b.group(1)
        dir2 = d4_b.group(2)
        dir3 = d4_b.group(3)
        dir4 = d4_b.group(4)
        header_name = d4_b.group(5) # should be the header file
        #print(dir1, dir2, dir3, dir4, dir5)
        dir1 = "inc\\" + dir1
        cmd1 = "mkdir " + dir1
        dir1_2 = dir1 + "\\" + dir2
        cmd2 = "mkdir " + dir1_2
        #print (dir1_2) 
        dir1_2_3 = dir1_2 + "\\" + dir3
        dir1_2_3_4 = dir1_2_3 + "\\" + dir4
        cmd3 = "mkdir " + dir1_2_3
        cmd4 = "mkdir " + dir1_2_3_4
        #print (dir1_2_3)
        #print (dir1_2_3_4)
        os.system(cmd1)
        os.system(cmd2)
        os.system(cmd3)
        os.system(cmd4)
        file_to_create = dir1_2_3_4 + "\\" + header_name
        #print(file_to_create)
        cmd5 = "touch " + file_to_create
        os.system(cmd5)
        #print (cmd1)
        return

def create_includes(filename):
    f = open(filename, "r")
    Lines = f.readlines()
    count = 1
    for line in Lines: 
        #print(line.strip()) 
        #print("Line{}: {}".format(count, line.strip()))
        x = re.search("^#include", line)
        if (x):
            print ("matched!", line)
            process_include_stmt(line)
        count = count + 1


file = open(get_filename(), "r")


print("file is", file.name)

cmd = "gcc -c " + file.name

#print(cmd)

# stdoutdata = subprocess.getoutput(cmd)

# print("stdoutdata: ") + stdoutdata

# for line in file:
# print line;

delete_inc()
create_inc()
create_includes(get_filename())
