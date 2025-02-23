import cv2
import os
import time
pth="D:\\videocap\\"
def video2pic(limit):
    cap = cv2.VideoCapture(0)
    i = 0
    while(1):
        ret,frame = cap.read()
        frame = cv2.flip(frame, 1) 
        cv2.imshow('capture',frame)
        cv2.imwrite(pth+ str(int(time.time()*1000//1)) + ".jpg",frame)
        i = i + 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if i >= limit:
            break
    cap.release()
    cv2.destroyAllWindows()

def video_demo():
    capture = cv2.VideoCapture(0)
    while(True):
        ret, frame = capture.read() 
        frame = cv2.flip(frame, 1) 
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

def video_capture():
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    fps = input("----你的视频帧率为多少？")
    fps=int(fps)
    size=input("----你的视频大小为多少？(例如：480*480)")
    size=size.split('*')
    out = cv2.VideoWriter('out\\result.mp4', fourcc, fps, (int(size[0]), int(size[1]))  )
    filelist = os.listdir(pth)
    for item in filelist:
        item=pth + item
        img=cv2.imread(item)
        img = cv2.resize(img, (int(size[0]), int(size[1])))
        out.write(img)

if __name__ == '__main__':
    chose=input('----请选择你的功能,1：测试摄像头2.实时拍摄视频3.把现有图片存入视频：')
    print("----(按下q键可以随时退出，照片保存在D:\\videocap中)----")
    if chose=='1':
        video_demo()
    if chose=='2' or chose=='3':
        if not os.path.exists('out'):
            os.makedirs('out')
        if chose=='2':
            filelist = os.listdir(pth)
            for item in filelist:
                os.remove(pth + item)
            limit = input("----你要拍摄多少帧照片？")
            video2pic(int(limit))
            video_capture()
        if chose=='3':
            video_capture()