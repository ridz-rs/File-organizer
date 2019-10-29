import os
from shutil import copy2
# file_types = {str: [{ }]}


def get_files(path):
    print(path)
    file_types = {".txt":[], ".ipynb": [], ".pdf": [], ".psd": [], ".ai": [],
                  ".pptx": [], ".png": [], ".jpg": [], ".mp3": [], ".wav": [],
                  ".svg": [], ".xd": [], ".id": [], ".mp4": [], ".dmg": [],
                  ".AUP": [], ".DAT": []}

    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            suffix = get_type(filename)
            # print(suffix)
            if suffix in file_types:
                p2 = path
                file_types[suffix].append(
                    {filename: os.path.join(p2, filename)})

        else:
            sub_file_types= get_files(os.path.join(path, filename))
            for key in file_types:
                file_types[key].extend(sub_file_types[key])

    return file_types


def copy_files_to(file_types, path):
    file_types = merge_data_files(file_types)  # merging data files with aup
    if not os.path.exists(path):
        os.mkdir(path)
    for key in file_types.keys():
        if key == '.DAT':
            continue
        new_path = os.path.join(path, key[1:])
        print(new_path)
        if os.path.exists(new_path)==False and len(file_types[key])>0:
            os.mkdir(new_path)
        for files in file_types[key]: # files is dictionary . keys= filenames. values = paths
            for name in files.keys():
                if len(file_types[key])> 0:
                    copy2(files[name], new_path)


def merge_data_files(file_types):
    for val in file_types['.DAT']:
        file_types['.AUP'].append(val)
    return file_types


def get_type(filename):
    i = filename.index('.')
    print(filename[i:])
    return filename[i:]


def has_a_number(filename):
    for c in filename:
        if c.is_digit():
            return True
    return False


def has_final_suggestion(filename):
    lst = ["final", "export", "complete", "completed"]
    for word in lst:
        if word in filename:
            return True
        else:
            return False


if __name__ == '__main__':
    # old_path = input("Enter the path you want to scan")
    old_path = os.path.join(os.getcwd(), 'Unorganized')
    file_types = get_files(old_path)
    print(file_types)
    # p = input("Enter where you want the organized files")
    p = os.path.join(os.getcwd(), 'Organized')
    copy_files_to(file_types, p)
