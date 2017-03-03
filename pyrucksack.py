import os
from settings import PROJECT_PATH as project_path, ROOT_PATH as root_path 
from datetime import datetime
import shutil

def backup_directory_creator():
    current = datetime.now()
    current_month = datetime.strftime(current, '%b')
    current_date = datetime.strftime(current, '%d')
    current_year = datetime.strftime(current, '%Y')
    backup_root_directory_name = root_path + "/" + ("%s") % (current_month)
    backup_directory_name = ("%s-%s") % (current_date, current_year)
    directory_name = os.path.join(backup_root_directory_name, backup_directory_name) 
    #root directory creator
    if not os.path.exists(backup_root_directory_name):
        os.makedirs(backup_root_directory_name)
    if os.path.exists(backup_root_directory_name) and not os.path.exists(directory_name):
        os.makedirs(directory_name)    
    
    return directory_name

def backup_creator(dst, symlinks=False, ignore=None):
    print dst
    for directory in range(len(project_path)):
        backup_directory = os.path.join(dst, project_path[directory])
        print os.path.join(dst, project_path[directory])
        if not os.path.exists(backup_directory):
            os.makedirs(backup_directory)

        # for item in os.listdir(backup_directory):
        #     source = os.path.join(backup_directory, item)
        #     destination = os.path.join(dst, item)
        #     if os.path.isdir(source):
        #         shutil.copytree(source, destination, symlinks, ignore)
        #     else:
        #         shutil.copy2(source, destination)   

if __name__ == "__main__":
    directory_name = backup_directory_creator()
    backup_creator(directory_name, symlinks=None, ignore=None)

