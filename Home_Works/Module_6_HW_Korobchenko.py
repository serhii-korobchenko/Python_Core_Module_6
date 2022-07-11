""" Backlog:
done by hand - 1. Create folder Garbage in Home_Work_folder
done by script - 2. Create folders: images, documents, audio, video, archives
3. Write recurcive function
   Script Requirements:
- sort all files by CATEGORIES:
                - pictures ('JPEG', 'PNG', 'JPG', 'SVG')
                - video    ('AVI', 'MP4', 'MOV', 'MKV')
                - documents ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
                - music     ('MP3', 'OGG', 'WAV', 'AMR')
                - archives  ('ZIP', 'GZ', 'TAR')
                - others    

    Expected results:
                - list of files in each CATEGORIES
                - list of all met EXTENSIONS 
                - list of all unfamiliar extensions 

4. Rename all files and folders by normalize function
5. Keep all extention immutable.
6. Delete all empty folders
7. Ignore folders: archives, video, audio, documents, images
8. All found archives unpack in the same name folder in archives folder
9. Do not rename files with unfamiliar extensons, but move them in Others folder.  """

import os
from pathlib import Path



### Set up main folder path
parent_dir = "D:\TEST\Garbage"
p = Path (parent_dir)

### Set up data containers
set_files_images = set()
set_files_documents = set()
set_files_audio = set()
set_files_video = set()
set_files_archives = set()
set_files_other = set()

set_met_extension = set()
set_unfam_extension = set()


### Create defined folders

list_folders_create = ['images', 'documents', 'audio', 'video', 'archives', 'other']

""" for item in list_folders_create:
    path = os.path.join(parent_dir, item)
    os.mkdir(path)
    print("Directory '% s' created" % item) """


print(f'Main folder is: {p}.')
### Create and open report txt file

report = open('report.txt', 'w')

# report.write(i.name + '\n')  --> final record from Sets




def search_function (path):   
    """ Function scan intendent folder at all levels of nestiness and find files and 
    folders with defined extensions.

    First parametr (path) - reveal carrent processing folder """

    for i in path.iterdir():
        on_print = '{:<30} {:<10}'.format(i.name, 'Folder' if i.is_dir() else 'File')
        print(on_print)
        report.write(on_print+ '\n')
        if i.is_dir():
            path_in = os.path.join(path, i)
            #search_function (path_in) # recursive case
       
search_function (p)

### Close report txt file
report.close()