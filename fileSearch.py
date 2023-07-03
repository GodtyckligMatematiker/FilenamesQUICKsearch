import sys
import os
import math
import subprocess

def create_init_files():
    name_to_paths = {}
    counter = 0
    def recurv_search(path):
        nonlocal counter


        if not os.path.exists(path):
            raise Exception("Path doesn't exist")
        try:
            for child in os.listdir(path + "/"):
                full_path = path + "/" + child

                if full_path in name_to_paths:
                    counter += 1

                    name_to_paths[child].append(path + "/")
                else:
                    counter += 1

                    name_to_paths[child] = [path + "/"]
                if os.path.isdir(full_path) > 0:
                    recurv_search(full_path)
        except Exception as e:
            print("couldn't get access too " + path)
            print(e)
    recurv_search("C:")
    print(counter)

    keys = list(name_to_paths.keys())
    keys.sort()
    sorted_name_to_paths = {i: name_to_paths[i] for i in keys}

    with open("./data/dummy.txt", "w") as f:
        for key in keys:
            try:
                f.write(key + "\n")
                f.write(str(sorted_name_to_paths[key]) + "\n")
            except Exception as e:
                print(e)
                sorted_name_to_paths.pop(key)

    with open('./data/filenames.txt', 'w') as f:
        #f.write(str(len(sorted_name_to_paths.keys())) + "\n")
        for key in sorted_name_to_paths.keys():
            #f.write(key + " " * (max_file_name_size - 1 - len(key)) + "\n")
            try:
                f.write(key + "\n")
            except Exception as e:

                print(e)


    with open('./data/filepaths.txt', 'w') as f:
        #f.write(str(len(sorted_name_to_paths.keys())) + "\n")
        for key in sorted_name_to_paths.keys():
            s = ' '.join(sorted_name_to_paths[key])
            s = s.replace('/', '\\')
            try:
                f.write(s + "\n")
            except Exception as  e:
                print(e)


if len(sys.argv) > 1:
    if sys.argv[1] == "init":
        create_init_files()
    else:
        target = sys.argv[1]
        if "filenames.txt" not in os.listdir("./data/") or "filepaths.txt" not in os.listdir("./data/"):
            raise Exception("Init has to be called before searching")
        with open("./data/filenames.txt", "r") as f:
            with open("./data/filepaths.txt", "r") as t:
                paths = t.readlines()
                lines = f.readlines()
                print(len(lines))
                print(len(paths))
                aMax = len(lines) - 1
                aMin = 0
                found = False
                while aMin <= aMax:
                    current = int((aMin + aMax)/2)

                    if target > lines[current][:-1]:
                        aMin = current + 1
                    elif target < lines[current][:-1]:
                        aMax = current - 1
                    else:
                        path = paths[current]
                        if len(path) > 3:
                            path = path[:-1]
                        print(path)
                        print(lines[current])
                        subprocess.Popen(fr'explorer "{path}"')
                        found = True
                        break
                if not found:
                    raise Exception("Couldn't find file")





else:
    raise Exception("Not enough arguments")
