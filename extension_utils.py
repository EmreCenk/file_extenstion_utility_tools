




import os
import requests
from typing import Iterable

def change_extension(path: str, new_extension: str = ".png" ):
    """
    :param path: path to the folder that contains all of the files
    :param new_extension: the new extension you want all the files to have
    :return: None
    """
    os.chdir(path)

    for file in os.listdir():
        name, type = os.path.splitext(file)
        if type != new_extension:
            os.rename(name, name + new_extension)



def download_all(pic_list: Iterable[str],
                 folder_path: str = "",
                 new_folder_name: str = "auto_download",
                 create_new: bool = True):
    """
    Utility function to download everything in a list of image source urls
    :param pic_list: list of picture source urls
    :param folder_path: path tot the folder you would like to save
    :param new_folder_name: name of the folder you would like to save this in
    :param create_new: Whether you want to create a new folder or not (aka use a previous one)
    :return:
    """
    original = os.getcwd()

    os.chdir(folder_path)

    index = 0

    if create_new:
        # trying to create a new folder with the given name. If the folder exists, we add a number to the end of the folder name
        # then try again
        while True:
            try: #trying to create the folder
                pathOfFolder = os.path.join(folder_path, f"{new_folder_name}{index}")
                os.mkdir(pathOfFolder)
                os.chdir(pathOfFolder)
                break
            except:
                # folder name already exists, increment the number at the end by one, then try agani
                index += 1

    else:
        # don't need to create a new folder
        pathOfFolder = os.path.join(folder_path, new_folder_name)
        os.chdir(pathOfFolder)

    # downloading all images:
    starting = len(os.listdir())
    for i in range(len(pic_list)):
        #making the request for the image:
        response = requests.get(pic_list[i])

        #writing the image to a file:
        file = open(f"d{starting + i}.png", "wb")
        file.write(response.content)
        file.close()

    os.chdir(original)


