import os
import shutil

path = input("enter path")
files = os.listdir(path)

for file in files:
    
    if os.path.isfile(os.path.join(path,file)):
        filename,extension = os.path.splitext(file)
    
        if os.path.exists(path+'/'+extension):
            shutil.move(path+'/'+file, path+'/'+extension)
        else:
            os.makedirs(path+'/'+extension)
            shutil.move(path+'/'+file, path+'/'+extension)