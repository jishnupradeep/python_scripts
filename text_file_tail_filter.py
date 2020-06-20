# Run this from the directory where all files are present.
# It created two directories 'Completed' and 'Failed' and move files accordingly and also generates a log file

import os
from os import path
import shutil

dir_complete = os.path.join(os.getcwd(), "Completed")
dir_failed = os.path.join(os.getcwd(), "Failed")
num_completed = 0
num_failed = 0

try:
    os.mkdir(dir_complete)
    os.mkdir(dir_failed)
except OSError:
    print ("Creation of the directories failed")
else:
    print ("Successfully created directories")


files = [i for i in os.listdir() if i.endswith(".txt")]
for f in files:
    with open(f, "r") as f1:
        last_line = f1.readlines()[-2]
    if "Completed" in last_line:
        shutil.move(os.path.join(os.getcwd(), f), os.path.join(dir_complete, f))
        num_completed += 1
    else:
        shutil.move(os.path.join(os.getcwd(), f), os.path.join(dir_failed, f))
        num_failed += 1

a = open("Result_Logs.txt", "w")
a.write("Completed LIMA Files (" + str(num_completed) + ")" + "\n_____________________\n")
for path, subdirs, files in os.walk(dir_complete):
   for filename in files:
     a.write(str(filename) + "\n")
a.write("\n\n\n\nFailed LIMA Files (" + str(num_failed) + ")" + "\n_____________________\n")
for path, subdirs, files in os.walk(dir_failed):
   for filename in files:
     a.write(str(filename) + "\n")
a.close()

print ("Completed: " + str(num_completed) + "\nFailed: " + str(num_failed) + "\nFilenames in Result_Logs.txt")