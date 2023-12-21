import json

# Instagram json -> txt

followers_json = "followers.json"
followers_txt = "followers.txt"
following_json = "following.json"
following_txt = "following.txt"


# For Followers
with open(followers_json, 'r') as json_file:
    json_data = json.load(json_file)

# Process and create the text content (modify this part as needed)
values = [entry["string_list_data"][0]["value"] for entry in json_data]

# Write the text content to the output file
with open(followers_txt, 'w') as text_file:
    for value in values:
        text_file.write(value + '\n')

# For Following
with open(following_json, 'r') as json_file:
    json_data = json.load(json_file)

# Process and create the text content (modify this part as needed)
# values = [entry["string_list_data"][0]["value"] for entry in json_data]
values = [entry["string_list_data"][0]["value"] for entry in json_data["relationships_following"]]

# Write the text content to the output file
with open(following_txt, 'w') as text_file:
    for value in values:
        text_file.write(value + '\n')









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