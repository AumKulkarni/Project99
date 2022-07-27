from importlib.resources import path
import os
import shutil
import time
 
def main():
    deleted_folders=0
    deleted_files=0
    path="C:\Users\Anuradha\OneDrive\Desktop\Snipping Tool"
    days=0
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds >= get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deleted_folders +=1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(root_folder,folder)
                    if seconds >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folders +=1
                for file in files:
                    file_path=os.path.join(root_folder,file)
                    if seconds >= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deleted_files +=1
        else:
            if seconds >= get_file_or_folder_age(path):
                remove_file(path)
                deleted_files +=1
    else:
        print(f'"(path)"is not found')
        deleted_files +=1
    print(f"deleted folders:(deleted_folders)")
    print(f"deleted files:(deleted_files)")
def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path}is removed successfully")
    else:
        print(f"unable to delete"+path)
def remove_file(path):
    if not os.remove(path):
        print(f"{path}is removed successfully")
    else:
        print(f"unable to delete"+path)
def get_file_or_folder_age(path):
    ctime=os.stat(path).st_ctime
    return ctime
if __name__ == '__main__':
    main()



            
    