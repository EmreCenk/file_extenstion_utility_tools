




import os
import requests
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



def download_all(pic_list):



    starting = len(os.listdir())
    for i in range(len(pic_list)):
        response = requests.get(pic_list[i])

        file = open(f"d{starting + i}.png", "wb")
        file.write(response.content)
        file.close()

