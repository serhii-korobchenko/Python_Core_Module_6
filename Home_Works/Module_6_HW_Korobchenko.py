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

4. Write functions for each category processing
5. Write normilize function:
6. Rename all files and folders by normalize function
7. Keep all extention immutable.
8. Delete all empty folders
9. Ignore folders: archives, video, audio, documents, images
10. All found archives unpack in the same name folder in archives folder
11. Do not rename files with unfamiliar extensons, but move them in Others folder.  """

import os
from pathlib import Path
import re



#SET_UPS######################################################3

### Set up target folder path
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

### Set_up for normilize function
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

# Create dict trans with help of zip()
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()




#DEF#################################################

def search_function (path, k_space):   
    """ Function scan intendent folder at all levels of nestiness and find files and 
    folders with defined extensions.

    First parametr (path) - reveal carrent processing folder
    Second parametr (k_space) - regulate emty space for diferenciation levels of nestiness """

    k_space += 1
    space = " " * 3 * k_space
    
    if len(os.listdir(path)) == 0: # base case
        # Delete empty folders
        #Path.rmdir(path)
        return 
    else:
        for i in path.iterdir():
            
            on_print = '{:<0} {:<30} {:<10}'.format(space, i.name, 'Folder' if i.is_dir() else 'File')
            print(on_print)
            report.write(on_print+ '\n')
            if i.is_dir():
                ### All our activities with folders

                # Rename by normalize function



                path = Path.joinpath(path, i)
                search_function (path, k_space) # recursive case
                
                # Delete empty folders
                if len(os.listdir(i)) == 0: 
                    Path.rmdir(i)
                print(i)
                
                #new_name = normalize (i)
                #os.renames(i, new_name)


            else:
                continue
                ### All our activities with files + archives

    k_space -= 1
    
    return k_space, set_files_images, set_files_documents, set_files_audio, set_files_video, set_files_archives, set_files_other

def namestr(obj, namespace):
    """ Function return name of veriable in string"""
    
    return [name for name in namespace if namespace[name] is obj]


def set_prep_for_write (set_x):
    """ Function write list of categories in report file"""

    with open('report.txt', 'a') as report:
        
        report.write(f'{namestr(set_x, globals())}: \n') 
        for item in set_x:
           report.write(str(item) + '\n') 
    return namestr(set_x, globals())



def normalize (name):
    """ Function normalize names files and folders"""
    
    p = name.translate(TRANS)
    result = re.sub(r'[^a-zA-Z0-9]', '_', p)
    return result

def process_pictures ():
    """ Function process pictures category"""
    
    pass

def process_video ():
    """ Function process video category"""
    
    pass

def process_documents ():
    """ Function process documents category"""
    
    pass

def process_music ():
    """ Function process music category"""
    
    pass

def process_archives ():
    """ Function process archives category"""
    
    pass

def process_others ():
    """ Function process others category"""
    
    pass

#MAIN_BODY########################################
print(f'Target folder is: {p}.')

with open('report.txt', 'w') as report:
    search_function (p, 0)
    report.write('\n\n\n')


print(set_prep_for_write (set_files_images))
print(normalize("Сергій;%:?%;?%;"))

    

    

