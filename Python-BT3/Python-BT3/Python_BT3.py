
import pygame
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry("150x200")

gameDisplay = pygame.display.set_mode((600,600))

a = tk.IntVar()
b = tk.IntVar()

v = tk.IntVar()

c = tk.IntVar()
c.set(0)


tk.Label(root, text="Choose your Graphics:",justify=tk.LEFT,padx=20).pack()

radiobutton1 = Radiobutton(root, variable = v, value = 0, text = "Rectangle", command =lambda: print(v.get()))
radiobutton2 = Radiobutton(root, variable = v, value = 1, text = "Ellipse", command =lambda: print(v.get()))

a = v.get()
b = c.get()


radiobutton1.pack()
radiobutton2.pack()

BG = (255,255,255)
R = 0
G = 0
B = 0
color = (R,G,B)

gameDisplay.fill(BG)

if(a == 0):
    R=255
if(a == 1):
    G=255
if(a == 2):
    B=255
if (b == 0 ):
    gameDisplay.fill(color)
if (b == 1 ):
    pygame.draw.polygon (gameDisplay, color, [ (300,0)  , (600,600) , (0,600) ])
if (b == 2 ):
    pygame.draw.ellipse(gameDisplay, (color), (0,0,600,600))
pygame.display.update()








root.mainloop()


    


    
