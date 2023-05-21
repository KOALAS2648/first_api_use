import tkinter as tk; root = tk.Tk()
from get_image import status_code, image_URL
from urllib.request import urlopen
from PIL import Image, ImageTk
image = urlopen(image_URL)
raw_image = image.read()
image.close()

photo = ImageTk.PhotoImage(data=raw_image)
label = tk.Label(image=photo)
label.pack()
# mainloop for tiknter
root.mainloop()