import json  

with open ("sample-data.json") as json_file:
    a  = json.load(json_file)
    
print(a)
