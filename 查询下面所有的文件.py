import os

path = "/Volumes/Extreme SSD/课程/Java黑马"  # 文件夹目录

path_list = []
rar_list = []  # 存放rar的路径


def getAbsolutePath(path):
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    for file in files:  # 遍历文件夹
        full_path = os.path.join(file, path)
        # 获取绝对路径
        absolutePath = full_path + "/" + file
        path_list.append(absolutePath)
    print(path_list)
    return path_list


def getUnderPath(absolutePath):
     getAbsolutePath(path)
     print(absolutePath)


