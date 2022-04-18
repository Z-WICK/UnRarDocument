import os
import rarfile


def Unrar(base_path, unPathPrefix, ifDelete):
    files = os.listdir(base_path)
    files.sort()
    for path in files:
        full_path = os.path.join(base_path, path)
        print("正在解压------->>>>" + path)
        try:
            z = rarfile.RarFile(full_path)
            UnTargetPath = base_path + "/Unrar-" + unPathPrefix + "/" + path[0:-4]
            z.extractall(UnTargetPath)
            z.close()
        except IsADirectoryError:
            print("该文件不需要解压")
            continue
        except Exception as e:
            print(e)
            continue

        if ifDelete == "y":
            try:
                os.remove(full_path)  # 删除源文件
                print("源文件-" + path[0:-4] + "\n已删除")
            except Exception as e:
                print(e)
