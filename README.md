# CC_GW_Parser
Carves out GW data out of wireshark pcap.

Instructions:

Install Bluestacks

Install Wireshark

Install Python 2.x (probably works on 3.x too)

Download or clone parse.py

Open parse.py in notepad or similar and modify the members list. Members list IS case sensitive.

Start capturing on Wireshark

Login to CC on bluestacks and go through gw pages.

Save the capture as plain text (Wireshark --> File --> Export Packet Dissections --> As Plain Text)


Run parse.py on the saved file via command line (cmd.exe)

  parse.py gw.txt > results.txt
  
Resulting output will be for easy copy paste ti War Data sheet:

  Points -- TAB -- might / 1000 

For each member as listed in the members list.
