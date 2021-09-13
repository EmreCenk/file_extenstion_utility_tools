




import os

def convert_all_to_png(path, new_extension = ".png" ):

    os.chdir(path)

    for file in os.listdir():
        name, type = os.path.splitext(file)
        if type != new_extension:
            os.rename(name, name + new_extension)



