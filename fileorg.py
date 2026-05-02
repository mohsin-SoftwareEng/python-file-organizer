import os
import shutil
path = "D:/MyData"
files = os.listdir(path)
print(files)
for file in files:
    name , ext = os.path.splitext(file)
    print(ext)
    if ext == ".png":
        os.makedirs(os.path.join(path, "Images"), exist_ok= True)
        shutil.move(os.path.join(path, file), os.path.join(path, "Images"))
    elif ext == ".pdf":
        os.makedirs(os.path.join(path, "Documents"), exist_ok= True)
        shutil.move(os.path.join(path, file), os.path.join(path, "Documents"))
    elif ext == ".mp4":
        os.makedirs(os.path.join(path, "Videos"), exist_ok= True)
        shutil.move(os.path.join(path, file), os.path.join(path, "Videos"))
    elif ext == ".jpeg":
        os.makedirs(os.path.join(path, "Images1"), exist_ok= True)
        shutil.move(os.path.join(path, file), os.path.join(path, "Images1"))
    elif ext == ".mkv":
        os.makedirs(os.path.join(path, "Videos1"), exist_ok= True)
        shutil.move(os.path.join(path, file), os.path.join(path, "Videos1"))
    elif ext == ".pptx":
        os.makedirs(os.path.join(path, "Documents1"), exist_ok= True)
        shutil.move(os.path.join(path, file), os.path.join(path, "Documents1"))
    

