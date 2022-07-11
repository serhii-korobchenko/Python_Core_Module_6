import shutil

### pack

#archive_name = shutil.make_archive('backup', 'zip') # Archive in the same folder

#archive_name = shutil.make_archive('backup', 'zip', 'D:\PYTHON\Python_Core_Module_6\Lectures') #Archive of other folder - Lectures

### unpack

#archive_name = shutil.make_archive('backup', 'zip', 'D:\PYTHON\Python_Core_Module_6\Lectures')
#shutil.unpack_archive(archive_name, 'D:\PYTHON\Python_Core_Module_6\Test folder') # unpack in Test folder

### Check supported archive formats
for shortcut, description in shutil.get_archive_formats():
    print('{:<10} | {:<10}'.format(shortcut, description))


