# CC_GW_Parser
Carves GW data out of wireshark pcap.

Instructions:

Install Bluestacks (http://www.bluestacks.com/)

Install Wireshark (https://www.wireshark.org/download.html)

Install Python 2.7 (https://www.python.org/download/releases/2.7/)

Download or clone parse.py

Open parse.py in notepad or similar and modify the members list. Members list IS case sensitive and the whole file IS space sensitive.

Start capturing on Wireshark

Login to CC on bluestacks and go through GW pages.

Save the capture as plain text (Wireshark --> File --> Export Packet Dissections --> As Plain Text)


Run parse.py on the saved file via command line (cmd.exe)

  parse.py gw.txt > results.txt
  
Resulting output will be easy copy paste to War Data sheet in the following format:

  Points -- TAB -- might / 1000 

For each member as listed in the members list.
