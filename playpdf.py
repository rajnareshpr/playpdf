import os
from PIL import Image
from merge_pdf import merge

print("Select an option:\n 1.Image to pdf converter\n 2.Pdf merges \n Note:- please make sure that pdf names are in sortable form.")
option = input()
source_dir = os.getcwd()

output_file = source_dir+"\\merged.pdf"
folder_files_pdf = source_dir

#Image to pdf converter
#for every file in directory
for file in os.listdir(source_dir):
        file_name, file_ext = os.path.splitext(file)

        if option == "1":
            if file.endswith(".jpg"):
                # loc = location of the file
                loc = Image.open(os.getcwd() +"\\"+ file_name+".jpg")
                loc.save(os.getcwd() +"\\"+ file_name+".pdf")
                print("Converting images to pdf completed.")
#pdf merger
if option == "2":
    merge.Merge (output_file).merge_folder (folder_files_pdf)
    print("Merging pdf completed")