class1_fn = input("class1 input file name: ")
class2_fn = input("class2 input file name: ")



#Open function to open the file
class1_fh = open(class1_fn)
class2_fh = open(class2_fn)



#class1
for line1 in class1_fh: 
    
    #removes excess leading/trailings lines
    line1 = line1.strip()
    #blank line? disregard
    if line1 == "":
        continue


    #print(line1[i] + ":")

    sent = 0
    
    #class2
    for line2 in class2_fh:
        
        #removes excess leading/trailings lines
        line2 = line2.strip()
        #blank line? disregard
        if line2 == "":
            continue
        #print("\t" + line2[j])
    
        if(line1 == line2):
            sent = 1
            break
    
    class2_fh.seek(0)

    if(sent == 0):
        print(line1)

    


#close the file handle
class1_fh.close()
class2_fh.close()
        


"""

class1 = following
class2 = followers

"""