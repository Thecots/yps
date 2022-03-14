from pynput import mouse
import pyautogui
import time
import win32api, win32con

# || zoom 125% 

# tablero
arr = []
x = 2926
y = 307
for i in range(9):
  ap = []
  for n in range(9):
    c = pyautogui.pixel(x+(40*i),y+(40*n))
    r = 0
    if(c[0] == 255 and c[1] == 255 and c[2] == 0): #yellow
      r = 'x'
    if(c[0] == 126 and c[1] == 126 and c[2] == 126): #default
      r = 0
    if(c[0] == 0 and c[1] == 0 and c[2] == 255): #blue 1
      r = 1
    if(c[0] == 0 and c[1] == 128 and c[2] == 0): #green 2
      r = 2
    if(c[0] == 255 and c[1] == 0 and c[2] == 0): #red 3
      r = 3
    ap.append(r)
  arr.append(ap)

#imprimir
for i in range(9):
  h = []
  for n in range(9):
    if arr[n][i] == 1:
      h.append([arr[n-1][i-1],arr[n][i-1],arr[n+1][i-1]])
      h.append([arr[n-1][i],arr[n][i],arr[n+1][i]])
      h.append([arr[n-1][i+1],arr[n][i+1],arr[n+1][i+1]])

      j = 0
      for i in range(3):
        for i in range(3):
          if(h[i][j] == 0):
            j += 1
      if j == 1:
        for i in range(3):
          for i in range(3):
            if(h[i][j] == 0):
              j += 1

print(h)



