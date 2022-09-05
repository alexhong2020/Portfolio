#following_fn = input("following input file name: ")
#followers_fn = input("followers input file name: ")

#Open function to open the file
following_fh = open("following.txt")
followers_fh = open("followers.txt")


set1 = set()
#following
for line1 in following_fh: 
    
    #removes excess leading/trailings lines
    line1 = line1.strip()
    #blank line? disregard
    if line1 == "":
        continue

    set1.add(line1)


set2 = set()   
#followers
for line2 in followers_fh:
        
    #removes excess leading/trailings lines
    line2 = line2.strip()
    #blank line? disregard
    if line2 == "":
        continue
    
    set2.add(line2)
    
    
print(set1.difference(set2)) 


#close the file handle
following_fh.close()
followers_fh.close()
        


"""

following = following
followers = followers

"""