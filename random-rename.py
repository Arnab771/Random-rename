import random
import os

path = '/home/arnab/Downloads/Images/'
orgNames = []
for (dirpath, dirname, filename) in os.walk(path):
    orgNames.extend(filename)

for name in orgNames:
    if name[-3: ] == "jpg" or name[-3: ] == "png" or name[-3: ] == "jpeg":
        randName = str(random.randint(45600, 78904)) + name[-4: ]
        os.rename(path + name, path + randName)
