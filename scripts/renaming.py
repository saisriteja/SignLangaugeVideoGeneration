import os

path = 'D:\\projects\\signlangauge\\scritps\\SignLangaugeVideoGeneration\\dataset1\\train_B'

for img in os.listdir(path):
    original = img.split('_')
    newname = original[0]+'.jpg'
    os.rename(os.path.join(path,img), os.path.join(path,newname))

# print(os.listdir(path))