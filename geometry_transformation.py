#Import Library
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from math import sin, cos, radians
from matplotlib import pyplot as plt

#Define Class
class GeometricTransformApp:
    def __init__(self, master):

        self.master = master
        
        # Create Array for vertex
        self.left_down = [0, 0]
        self.right_down = [5, 0]
        self.right_up = [5, 5]
        self.left_up = [0, 5]

        self.vertex_a = np.array(self.left_down)
        self.vertex_b = np.array(self.right_down)
        self.vertex_c = np.array(self.right_up)
        self.vertex_d = np.array(self.left_up)

        
        # Create the buttons
        scale_buttonframe = tk.Frame(buttonframe)
        scale_buttonframe.pack(pady=15)
        label_scale_buttonframe = tk.Label(scale_buttonframe, text="Scaling")
        label_scale_buttonframe.pack(pady=10)

        rotate_buttonframe = tk.Frame(buttonframe)
        rotate_buttonframe.pack(pady=15)
        label_rotate_buttonframe = tk.Label(rotate_buttonframe, text="Rotating")
        label_rotate_buttonframe.pack(pady=10)

        translate_buttonframe = tk.Frame(buttonframe)
        translate_buttonframe.pack(pady=15)
        label_translate_buttonframe = tk.Label(translate_buttonframe, text="Translating")
        label_translate_buttonframe.pack(pady=10)

        reset_buttonframe = tk.Frame(buttonframe)
        reset_buttonframe.pack(pady=20)
        label_reset_buttonframe = tk.Label(reset_buttonframe, text="Reset Shape")
        label_reset_buttonframe.pack(pady=10)

        up_translate_buttonframe = tk.Frame(translate_buttonframe)
        up_translate_buttonframe.pack(pady=8)       
        lr_translate_buttonframe = tk.Frame(translate_buttonframe)
        lr_translate_buttonframe.pack(pady=8)       
        down_translate_buttonframe = tk.Frame(translate_buttonframe)
        down_translate_buttonframe.pack(pady=8)       
              
        
        self.scale_button_big = tk.Button(scale_buttonframe, text="Scale Big", command=self.dilatation_big)
        self.scale_button_big.pack(side=tk.LEFT, padx=5)

        self.scale_button_small = tk.Button(scale_buttonframe, text="Scale Small", command=self.dilatation_small)
        self.scale_button_small.pack(side=tk.LEFT, padx=5)

        self.rotate_button_anticw = tk.Button(rotate_buttonframe, text="Rotate Anticlockwise", command=self.rotation_anticlockwise)
        self.rotate_button_anticw.pack(side=tk.LEFT, padx=5)

        self.rotate_button_cw = tk.Button(rotate_buttonframe, text="Rotate Clockwise", command=self.rotation_clockwise)
        self.rotate_button_cw.pack(side=tk.LEFT, padx=5)

        self.translate_button_up = tk.Button(up_translate_buttonframe, text="Translate Up", command=self.translation_up)
        self.translate_button_up.pack(padx=10)

        self.translate_button_left = tk.Button(lr_translate_buttonframe, text="Translate Left", command=self.translation_left)
        self.translate_button_left.pack(side=tk.LEFT, padx=10)

        self.translate_button_right = tk.Button(lr_translate_buttonframe, text="Translate Right", command=self.translation_right)
        self.translate_button_right.pack(side=tk.LEFT, padx=10)


        self.translate_button_down = tk.Button(down_translate_buttonframe, text="Translate Down", command=self.translation_down)
        self.translate_button_down.pack(side=tk.BOTTOM, padx=10)
    
        self.reset_button = tk.Button(reset_buttonframe, text="Reset", command=self.reset_position)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        
        #Draw square based on vertex
        self.draw_polygon(self.vertex_a,self.vertex_b,self.vertex_c,self.vertex_d)
        self.update_polygon(self.vertex_a,self.vertex_b,self.vertex_c,self.vertex_d)
    
    #Define function for rotation
    def rotation(self, arah):
        sudut = 90*arah
        titik_putar = [0,0]
        rotation_matrix = np.array([[round(cos(radians(sudut)),3),round(sin(radians(sudut)),3)*-1,0],
                                    [round(sin(radians(sudut)),3),round(cos(radians(sudut)),3),0],
                                    [0,0,1]])

        #Ubah titik menjadi 3 dimensi
        self.vertex_a = np.append(self.vertex_a,1)
        self.vertex_a = np.matmul(rotation_matrix,self.vertex_a)
        self.vertex_a = np.delete(self.vertex_a, -1, axis = 0)
        self.vertex_b = np.append(self.vertex_b,1)
        self.vertex_b = np.matmul(rotation_matrix,self.vertex_b)
        self.vertex_b = np.delete(self.vertex_b, -1, axis = 0)
        self.vertex_c = np.append(self.vertex_c,1)
        self.vertex_c = np.matmul(rotation_matrix,self.vertex_c)
        self.vertex_c = np.delete(self.vertex_c, -1, axis = 0)
        self.vertex_d = np.append(self.vertex_d,1)
        self.vertex_d = np.matmul(rotation_matrix,self.vertex_d)
        self.vertex_d = np.delete(self.vertex_d, -1, axis = 0)

        self.update_polygon(self.vertex_a,self.vertex_b,self.vertex_c,self.vertex_d)

    #Define function for anti-clockwise rotation
    def rotation_anticlockwise(self):
        arah = 1
        self.rotation(arah)

    #Define function for clockwise rotation
    def rotation_clockwise(self):
        arah = -1
        self.rotation(arah)

    #Define function for Dilatation
    def dilatation(self, x, y):
        dilatation_matrix = np.array([[x,0,0],
                                      [0,y,0],
                                      [0,0,1]])

        #Ubah titik menjadi 3 dimensi
        self.vertex_a = np.append(self.vertex_a,1)
        self.vertex_a = np.matmul(dilatation_matrix,self.vertex_a)
        self.vertex_a = np.delete(self.vertex_a, -1, axis = 0)
        self.vertex_b = np.append(self.vertex_b,1)
        self.vertex_b = np.matmul(dilatation_matrix,self.vertex_b)
        self.vertex_b = np.delete(self.vertex_b, -1, axis = 0)
        self.vertex_c = np.append(self.vertex_c,1)
        self.vertex_c = np.matmul(dilatation_matrix,self.vertex_c)
        self.vertex_c = np.delete(self.vertex_c, -1, axis = 0)
        self.vertex_d = np.append(self.vertex_d,1)
        self.vertex_d = np.matmul(dilatation_matrix,self.vertex_d)
        self.vertex_d = np.delete(self.vertex_d, -1, axis = 0)

        self.update_polygon(self.vertex_a,self.vertex_b,self.vertex_c,self.vertex_d)

    #Define function for big dilatation
    def dilatation_big(self):
        x = 2
        y = 2
        self.dilatation(x, y)

    #Define function for small dilatation
    def dilatation_small(self):
        x = 0.5
        y = 0.5
        self.dilatation(x, y)
    
    #Define function for Translation
    def translation(self,x,y):
        translation_matrix = np.array([[1,0,x],
                                 [0,1,y],
                                 [0,0,1]])

        #Ubah titik menjadi 3 dimensi
        self.vertex_a = np.append(self.vertex_a,1)
        self.vertex_a = np.matmul(translation_matrix,self.vertex_a)
        self.vertex_a = np.delete(self.vertex_a, -1, axis = 0)
        self.vertex_b = np.append(self.vertex_b,1)
        self.vertex_b = np.matmul(translation_matrix,self.vertex_b)
        self.vertex_b = np.delete(self.vertex_b, -1, axis = 0)
        self.vertex_c = np.append(self.vertex_c,1)
        self.vertex_c = np.matmul(translation_matrix,self.vertex_c)
        self.vertex_c = np.delete(self.vertex_c, -1, axis = 0)
        self.vertex_d = np.append(self.vertex_d,1)
        self.vertex_d = np.matmul(translation_matrix,self.vertex_d)
        self.vertex_d = np.delete(self.vertex_d, -1, axis = 0)

        self.update_polygon(self.vertex_a,self.vertex_b,self.vertex_c,self.vertex_d)
 
    #Define function for Left Translation
    def translation_left(self):
        x = -5
        y = 0
        self.translation(x,y)

    #Define function for Right Translation
    def translation_right(self):
        x = 5
        y = 0
        self.translation(x,y)

    #Define function for Up Translation
    def translation_up(self):
        x = 0
        y = 5
        self.translation(x,y)

    #Define function for Down Translation
    def translation_down(self):
        x = 0
        y = -5
        self.translation(x,y)


    #Define function for plotting square
    def draw_polygon(self, a, b, c, d):
        self.fig, self.ax = plt.subplots()
        plt.plot([a[0],b[0]],[a[1],b[1]],'k-')
        plt.plot([b[0],c[0]],[b[1],c[1]],'k-')
        plt.plot([c[0],d[0]],[c[1],d[1]],'k-')
        plt.plot([d[0],a[0]],[d[1],a[1]],'k-')
        plt.grid()
        self.ax.set_aspect('equal')
        plt.xlim(-25,25)
        plt.ylim(-25,25)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    #Define function for updating square
    def update_polygon(self, a, b, c, d):
        self.canvas.get_tk_widget().destroy()
        self.fig.clf()
        plt.plot([a[0],b[0]],[a[1],b[1]],'k-')
        plt.plot([b[0],c[0]],[b[1],c[1]],'k-')
        plt.plot([c[0],d[0]],[c[1],d[1]],'k-')
        plt.plot([d[0],a[0]],[d[1],a[1]],'k-')
        plt.grid()
        self.ax.set_aspect('equal')
        plt.xlim(-25,25)
        plt.ylim(-25,25)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.RIGHT)
    
    #Define function for restart square position to default position
    def reset_position(self):
        self.left_down = [0, 0]
        self.right_down = [5, 0]
        self.right_up = [5, 5]
        self.left_up = [0, 5]


        self.vertex_a = np.array(self.left_down)
        self.vertex_b = np.array(self.right_down)
        self.vertex_c = np.array(self.right_up)
        self.vertex_d = np.array(self.left_up)

        self.update_polygon(self.vertex_a,self.vertex_b,self.vertex_c,self.vertex_d)


# Create a new instance of Tkinter window
root = tk.Tk()
root.title("Transformasi Geometri App V3")
label = tk.Label(root, text="Program Transformasi Geometri bangun datar")
label.pack()
buttonframe = tk.Frame(root)
buttonframe.pack( side = tk.LEFT )
app = GeometricTransformApp(root)
root.mainloop()
