




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



def download_all(pic_list,
                 folder_path = r"C:\Users\emrec\Desktop\Emre1\Programming\stuff\things\dp_",
                 new_folder_name = "auto_download",
                 create_new = True):
    original = os.getcwd()

    os.chdir(folder_path)

    index = 0

    if create_new:
        while True:
            try:
                pathOfFolder = os.path.join(folder_path, f"{new_folder_name}{index}")
                os.mkdir(pathOfFolder)
                os.chdir(pathOfFolder)
                break
            except:
                index += 1

    else:
        pathOfFolder = os.path.join(folder_path, new_folder_name)
        os.chdir(pathOfFolder)

    starting = len(os.listdir())
    for i in range(len(pic_list)):
        response = requests.get(pic_list[i])

        file = open(f"d{starting + i}.png", "wb")
        file.write(response.content)
        file.close()

    os.chdir(original)


