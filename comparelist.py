#compare two lists and print the differences


#opens first file to compare
with open("file1.txt") as file1list:
        file1l = file1list.read().splitlines()
        
#opens second file to compare
with open("file2.txt") as file2list:
        file21 = file2list.read().splitlines()
        
#assigns files to sets
set1=file1l
set2=file2l

#Prints everything in set b that's not in set a

def difference(a, b):
    return list(set(b).difference(set(a)))

list_diff=difference(set1,set2)

print list_diff
