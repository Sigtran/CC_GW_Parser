import sys, struct, codecs
from itertools import islice

members = [
'Aggrriify',
'akateksahn',
'aversai',
'Beef3687',
'btgreat',
'BuuDeV',
'CanadianCnote',
'candianhayden',
'CCraider',
'Chrismurf16',
'Classydame',
'DaDavemanCan',
'davh9',
'Demongamefreak',
'Diederik69',
'DrYoshiro',
'EasyEgon',
'EasyEgon777',
'Featherstep',
'GarrethXX',
'gemzilou',
'GGGkz',
'Haidez',
'hoskie',
'iyyi',
'jro012',
'LazyMisted',
'Lisk0',
'logicbomb',
'LordTwinkle',
'mixhael',
'MJMFOX',
'MrPerfect988',
'Neit007',
'Noxv',
'Pinchmiestro',
'Piremard96',
'quackpatton',
'Sandmen',
'Sarhezor',
'Sicknessi',
'Sigtrah',
'Sigtran',
'slicksean',
'Tappoman',
'thefrfcfgcc',
'tospeli',
'Tracebot21',
'TrueDaBoMb',
'truewarwizard',
'VexApex',
'Voobb',
'whipplash',
'xd4rkr4iderx',
'yujamigit',
'zoofo',
'Zula1810'
    ]

results = {}


with open(sys.argv[1], "rb") as f:
    for line in f:
        for member in members:
            if '   '+member+'.' in line:
                data = ''.join(islice(f,1,2)).replace(" ", "")
                #print member, data
                might = (struct.unpack("<I", codecs.decode(data[4:12], "hex"))[0])/1000
                score = struct.unpack("<h", codecs.decode(data[12:16], "hex"))[0]
                results[member] = str(score) + '\t' + str(might)

for member in members:
    try:
        #print member +'\t', results[member]
        print results[member]
    except:
        print member, 'NOT FOUND'
