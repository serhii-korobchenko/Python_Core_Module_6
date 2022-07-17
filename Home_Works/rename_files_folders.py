
import os
import re
from pathlib import Path


### Set_up for normilize function
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

# Create dict trans with help of zip()
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize (name):
    """ Function normalize names files and folders"""
    
    p = name.translate(TRANS)
    result = re.sub(r'[^a-zA-Z0-9\.]', '_', p)
    return result

def rename_func (path):

    path_file_item = Path (path)
    path_folder_item = path_file_item.parent.absolute()
    old_name = os.path.basename(path_file_item)               
    new_name = normalize (old_name)
    new_name_path = Path.joinpath(path_folder_item, new_name)



    if new_name != old_name:
        os.rename(path_file_item, new_name_path, src_dir_fd=None, dst_dir_fd=None)

        
    
print(rename_func('D:\TEST\Garbage\\alfa\Керівництво Alpha Now_Eng.docx'))