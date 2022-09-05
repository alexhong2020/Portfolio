following_fn = input("following input file name: ")
followers_fn = input("followers input file name: ")

#Open function to open the file
following_fh = open(following_fn)
followers_fh = open(followers_fn)


#following
for line1 in following_fh: 
    
    #removes excess leading/trailings lines
    line1 = line1.strip()
    #blank line? disregard
    if line1 == "":
        continue


    sent = 0
    
    #followers
    for line2 in followers_fh:
        
        #removes excess leading/trailings lines
        line2 = line2.strip()
        #blank line? disregard
        if line2 == "":
            continue
    
        if(line1 == line2):
            sent = 1
            break
    
    followers_fh.seek(0)

    if(sent == 0):
        print(line1)


#close the file handle
following_fh.close()
followers_fh.close()
        
