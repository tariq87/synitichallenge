import json
with open('data.json') as f:
	data = json.load(f)

x = 1
ids = []
for i in range(1,len(data)):
    #checking non empty string
    if ('name' in data[i-x] and 'zip' in data[i-x] and 'address' in data[i-x]) and ('name' in data[i] and 'zip' in data[i] and 'address' in data[i]) :
	    if (data[i-x]['name'] is None or len(data[i-x]['name'])==0) or (data[i-x]['zip'] is None or len(data[i-x]['zip'])==0) or (data[i-x]['address'] is None or len(data[i-x]['address'])==0):
	    	ids.append(data[i-x]['id'])
    
    #checking for duplicates
		if (data[i-x]['name'] == data[i]['name']) and (data[i-x]['zip'] == data[i]['zip']) and (data[i-x]['address'] == data[i]['address']):
			ids.append(data[i-x]['id'])
			ids.append(data[i]['id'])
for i in ids:
	print(i)
