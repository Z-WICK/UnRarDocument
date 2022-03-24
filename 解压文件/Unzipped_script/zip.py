import os
import zipfile


def UnZip(base_path, unPathPrefix, ifDelete):
    files = os.listdir(base_path)
    files.sort()
    for path in files:
        full_path = os.path.join(base_path, path)
        print("正在解压----->>>" + path)

        try:
            zFile = zipfile.ZipFile(full_path, "r")
            # ZipFile.namelist(): 获取ZIP文档内所有文件的名称列表
            for fileM in zFile.namelist():
                UnTargetPath = base_path + "/UnZip-" + unPathPrefix + "/" + path[0:-4]
                zFile.extract(fileM, UnTargetPath)
                zFile.close()
        except IsADirectoryError:
            print("该文件不需要解压")
            continue
        except Exception:
            print(path[0:-4] + "该文件有误")
            print("该文件可能是Rar等其他格式的压缩文件")
            continue

        if ifDelete == "y":
            try:
                os.remove(full_path)  # 删除源文件
                print("源文件-" + path[0:-4] + "\n已删除")
            except Exception:
                print("文件异常")










