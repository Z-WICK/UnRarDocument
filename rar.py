import os
import rarfile

print("非rar不解压！！！")


def unrar(base_path, unPathPrefix, ifDelete):
    files = os.listdir(base_path)
    files.sort()
    i = 0
    for path in files:
        full_path = os.path.join(base_path, path)
        print("正在解压-\n" + base_path)
        try:
            z = rarfile.RarFile(full_path)
            z.extractall(base_path + "/Unrar-" + unPathPrefix + "/" + path[0:-4])
            z.close()
        except IsADirectoryError:
            print("该文件不需要解压")
            continue
        except Exception:
            print(path[0:-4] + "该文件有误")
            print("该文件可能是zip等其他格式的压缩文件")
            continue

        if ifDelete == "y":
            try:
                os.remove(full_path)  # 删除源文件
                print("源文件-" + path[0:-4] + "\n已删除")
            except Exception:
                print("文件异常")


while True:
    unPathPrefix = input("输入---解压---到指定目录：")
    ifDelete = input("解压后是否删除源文件：y/n：")
    base_path = input("输入需要解压的路径：")
    unrar(base_path, unPathPrefix, ifDelete)

    ifContinue = input("是否继续解压？y/n:")
    if ifContinue == "n":
        break
