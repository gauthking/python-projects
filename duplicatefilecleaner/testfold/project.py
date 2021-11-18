import os 
import filecmp

path=os.chdir("C:\\Users\\USER\\Desktop\\programcodestuff\\python\\pythonprojects\\duplicatefilecleaner\\testfold")
file_list=os.listdir(path)
print(file_list)
print("Enter the file name along with the extension:")
s=input()
for i in file_list:
    if i!=s:
        if filecmp.cmp(s,i,shallow=True):
            os.remove(i)
            print("file deleted:",i)

#CLONE THE DUPLICATE FILE CLEANER FOLDER INTO YOUR SYSTEM.
#ENTER THE NAME OF THE FILE AS '2086970.jpg'
#THE PROGRAM WILL DELETE ALL THE DUPLICATES OF THE SPECIFIED FILE NAME