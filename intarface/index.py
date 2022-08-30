import tkinter as tk
from tkinter import filedialog
import os

# def UploadAction():
    # os.system('%windir%\\System32\\cmd.exe "/K" C:\\Users\\Abdellah\\anaconda3\\Scripts\\activate.bat')
    # os.system('conda activate yolov4-cpu')
    # os.system('python object_tracker.py --video ./data/video/test.mp4 --output ./outputs/demo.avi --model yolov4')
    # filename = filedialog.askopenfilename()
    # print('Selected:', filename)
    
def c1():
    os.system('%windir%\\System32\\cmd.exe "/K" C:\\Users\\Abdellah\\anaconda3\\Scripts\\activate.bat')

def c2():
    os.system('conda activate yolov4-cpu')

def c3():
    os.system('python object_tracker.py --video ./data/video/test.mp4 --output ./outputs/demo.avi --model yolov4')

def c():
    c1()
    c2()
    c3()

root = tk.Tk()
button = tk.Button(root, text='Open', command=c1)
button.pack()
button2 = tk.Button(root, text='Open', command=c2)
button2.pack()
button3 = tk.Button(root, text='Open', command=c3)
button3.pack()

root.mainloop()




# import tkinter as tk
# import cv2
# from PIL import Image, ImageTk

# width, height = 800, 600
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# root = tk.Tk()
# root.bind('<Escape>', lambda e: root.quit())
# lmain = tk.Label(root)
# lmain.pack()

# def show_frame():
#     _, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
#     img = Image.fromarray(cv2image)
#     imgtk = ImageTk.PhotoImage(image=img)
#     lmain.imgtk = imgtk
#     lmain.configure(image=imgtk)
#     lmain.after(10, show_frame)

# show_frame()
# root.mainloop()
