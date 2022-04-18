import cv2
import os

path = input("复制视频文件夹路径:")
single_file_path = os.listdir(path)  # 路径下面的视频名字列表


def capFrame(videoPath, savePath):
    cap = cv2.VideoCapture(videoPath)
    numFrame = 0
    while True:
        if cap.grab():
            numFrame += 1
            # 每60桢截取一个图片
            if numFrame % 60 == 1:
                # retrieve 解码并返回一个桢
                flag, frame = cap.retrieve()
                if not flag:
                    continue
                else:
                    cv2.imshow('video', frame)
                    newPath = savePath + "\\" + str(int(numFrame / 60)) + ".jpg"
                    cv2.imencode('.jpg', frame)[1].tofile(newPath)
        # 检测到按下Esc时，break（和imshow配合使用）
        # if cv2.waitKey(10) == 27:
        # if len(os.listdir()) == 10:
        #     print(len(os.listdir()))
        break


for file_path in single_file_path:  # 循环列表获得单个路径
    get_img_path = path + "/" + file_path  # 视频的绝对路径
    capFrame(get_img_path, get_img_path)
