class1_fn = input("class1 input file name: ")
class2_fn = input("class2 input file name: ")

#Open function to open the file
class1_fh = open(class1_fn)
class2_fh = open(class2_fn)


set1 = set()
#class1
for line1 in class1_fh: 
    
    #removes excess leading/trailings lines
    line1 = line1.strip()
    #blank line? disregard
    if line1 == "":
        continue

    set1.add(line1)


set2 = set()   
#class2
for line2 in class2_fh:
        
    #removes excess leading/trailings lines
    line2 = line2.strip()
    #blank line? disregard
    if line2 == "":
        continue
    
    set2.add(line2)
    
    
print(set1.difference(set2)) 


#close the file handle
class1_fh.close()
class2_fh.close()
        


"""

class1 = following
class2 = followers

"""