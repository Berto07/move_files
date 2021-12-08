import os, shutil

#Replace the directory source and destination. 
source_folder = r"/Users/Beto/Documents/untitled_folder" 

destination_folder = r"/Users/Beto/Documents/untitled_folder1"

files = os.listdir(source_folder)
files2 = os.listdir(destination_folder)

print(os.chdir(source_folder))

for file in files:
    if os.path.isfile(file):
        shutil.move(file, destination_folder)
