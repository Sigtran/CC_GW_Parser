import sys, struct, codecs
from itertools import islice

members = [
"Aggrriify",
"akateksahn",
"BuuDeV",
"Chrismurf16",
"DaDavemanCan",
"davh9",
"DrYoshiro",
"EasyEgon",
"Featherstep",
"FrontalNgagemnT",
"govnosrach",
"greenxpg",
"Haidez",
"hegolas",
"hegolas3",
"hoskie",
"kokkaburra",
"logicbomb",
"MJMFOX",
"Monzarelli",
"mrBira",
"nebzdyashi",
"Pinchmiestro",
"Pinchster",
"Sarhezor",
"Sicknessi",
"Sigtrah",
"Sigtran",
"slicksean",
"storochbrun",
"Tappoman",
"tospeli",
"truewarwizard",
"VexApex"
    ]

results = {}


with open("gw.txt", "rb") as f:
    for line in f:
        for member in members:
            if '   '+member+'.' in line:
                data = ''.join(islice(f,1,2)).replace(" ", "")
                #print member, data
                might = (struct.unpack("<I", codecs.decode(data[4:12], "hex"))[0])/1000
                score = struct.unpack("<h", codecs.decode(data[12:16], "hex"))[0]
                if score > 0 or member not in results:
			        results[member] = str(score) + '\t' + str(might) #+ '\r\n'

#with open("results.txt", "wb") as f:
for member in members:
	try:
		#print member +'\t', results[member]
		#f.write(results[member])
		print results[member]
	except:
		#f.write(results[member])	
		print member, 'NOT FOUND'
