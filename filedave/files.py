import os
# r = read 
# a = append / update
# w = write
# x = create

# read - error if it doesnt exist

f = open("names.txt")
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("names.txt")
    print(f.read())
except: 
    print("The file you want to read dosen't exist")
finally:
    f.close()

# Append - creates a file that doesn't exist
f = open("names.txt", "a")
f.write("neil\n")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# write (overwrite)
f = open("contex.txt", "w")
f.write("i deleted all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing, create the file if it doesn't exist
f = open("name_list.txt", "w")
f.close()

# creates the specific file, but returns an error if the file exist
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

# delete a file

# avoid an error if it doesn't exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("the file  you wish to delete doesn't exist")


with open("morenames.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)