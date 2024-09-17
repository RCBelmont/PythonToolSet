import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL.Image import Resampling

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        img = Image.open(file_path)
        (width, height) = img.size
        new_height = height * 768 // width
        img = img.resize((768, new_height), Resampling.BILINEAR)  # 调整图片大小
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        canvas.image_tk = img_tk
        canvas.image = img
        canvas.true_size = (768, new_height)

def mark_point(event):
    if canvas.image:
        x, y = event.x, event.y
        if x < 768 and y < canvas.true_size[1]:
            print(f"Marked point at: ({x}, {y})")
            p_size = 5
            canvas.create_oval(x-p_size, y-p_size, x+p_size, y+p_size, fill='red')
            if canvas.image:
                print(canvas.image.getpixel((x, y)))

def clear_points():
    canvas.delete("all")


root = tk.Tk()
root.title("Image Picker")
root.geometry("800x600")

btn = tk.Button(root, text="选择图片", command=open_image)
btn.pack()
btn_clear = tk.Button(root, text="清空标点", command=clear_points)
btn_clear.pack()

canvas = tk.Canvas(root, width=768, height=768)
canvas.pack()
canvas.image = None



canvas.bind("<Button-1>", mark_point)

root.mainloop()