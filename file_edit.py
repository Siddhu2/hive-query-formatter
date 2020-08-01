import os
import re

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

my_file = os.path.join(THIS_FOLDER, 'sample.txt')
text_file = open("Output.txt", "w")

with open(my_file,'r') as file:
    q = file.read()

edited = " ".join(q.split())
edited = re.sub(r'\s*,\s*', ',', edited)
text_file.write(edited)
text_file.close()
#print (edited)