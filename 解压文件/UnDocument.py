from 解压文件.Unzipped_script.rar import Unrar
from 解压文件.Unzipped_script.tar import Untar
from 解压文件.Unzipped_script.zip import UnZip


def choose_fun():
    try:
        print("1.我都要"
              "\n2.zip"
              "\n3.rar"
              "\n4.tar")
        choose_fun = int(input("输入你需要的解压的格式："))
        return choose_fun
    except ValueError:
        print("输入的值有误")


def Unzip_parameters():
    base_path = input("输入需要解压的路径：")
    unPathPrefix = input("输入---解压---到指定目录：")
    ifDelete = input("解压后是否删除源文件：y/n：")
    return base_path, unPathPrefix, ifDelete


while True:
    function_num = choose_fun()

    if function_num == 1:  # 我都要
        Un_param = Unzip_parameters()
        Unrar(Un_param[0], Un_param[1], Un_param[2])
        UnZip(Un_param[0], Un_param[1], Un_param[2])
        Untar(Un_param[0], Un_param[1], Un_param[2])


    elif function_num == 2:  # 解压ZIP
        Un_param = Unzip_parameters()
        UnZip(Un_param[0], Un_param[1], Un_param[2])

    elif function_num == 3:  # 解压RAR
        Un_param = Unzip_parameters()
        Unrar(Un_param[0], Un_param[1], Un_param[2])

    elif function_num == 4:  # tar
        Un_param = Unzip_parameters()
        Untar(Un_param[0], Un_param[1], Un_param[2])

    ifContinue = input("是否继续解压？y/n:")
    if ifContinue == "n":
        break
