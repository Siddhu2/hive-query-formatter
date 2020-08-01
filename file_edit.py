import os,re,sys

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

if len(sys.argv) < 3:
   print('Usage: python file-edit.py [source_file_name] [edited_file_name]')
   sys.exit()

source_file = sys.argv[1]
target_file = sys.argv[2]
my_file = os.path.join(THIS_FOLDER, source_file)
text_file = open(target_file, "w")

with open(my_file,'r') as file:
    q = file.read()

edited = " ".join(q.split())
edited = re.sub(r'\s*,\s*', ',', edited)
text_file.write(edited)
text_file.close()
#print (edited)