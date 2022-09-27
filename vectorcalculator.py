# -*- coding: utf-8 -*-
"""
@author: Andrew
"""
#Andrew Chen
#Vecotr Calculator


#import statements 
import matplotlib
matplotlib.use("TkAgg")
from tkinter import *
import numpy as np
import math

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from matplotlib.figure import Figure

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
    from Tkinter import ttk
else:
    import tkinter as Tk
    from tkinter import ttk
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt




#Application code - GUI
class Application(Frame):
    """ GUI application that calculates vector related numbers based on user input. """
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets to input info. """
        
        #Labels for output
        Label(self,
              text = "Dot Product"
              ).grid(row = 0, column = 75, columnspan = 2, sticky = W)
        Label(self,
              text = "Cross Product"
              ).grid(row = 0, column = 200, columnspan = 2, sticky = W)
        Label(self,
              text = "Magnitude of Vector 1"
              ).grid(row = 4, column = 75, columnspan = 2, sticky = W)
        Label(self,
              text = "Magnitude of Vector 2"
              ).grid(row = 4, column = 200, columnspan = 2, sticky = W)
        Label(self,
              text = "Unit Vector 1"
              ).grid(row = 8, column = 75, columnspan = 2, sticky = W)
        Label(self,
              text = "Unit Vector 2"
              ).grid(row = 8, column = 200, columnspan = 2, sticky = W)
        Label(self,
              text = "Component of Vector 1 on Vector 2"
              ).grid(row = 12, column = 75, columnspan = 2, sticky = W)
        Label(self,
              text = "Component of Vector 2 on Vector 1"
              ).grid(row = 12, column = 200, columnspan = 2, sticky = W)
        Label(self,
              text = "Projection of Vector 1 on Vector 2"
              ).grid(row = 16, column = 75, columnspan = 2, sticky = W)
        Label(self,
              text = "Projection of Vector 2 on Vector 1"
              ).grid(row = 16, column = 200, columnspan = 2, sticky = W)
        
        
        ##Vector 1###################
        Label(self,
              text = "Enter the components of Vector 1:\
              \nNote: The program will only take numbers."
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
        Label(self,
              text = "Vector 1:"
              ).grid(row = 18, column = 0, columnspan = 2, sticky = W)

        # create labels for xyz
        Label(self,
              text = "X: "
              ).grid(row = 1, column = 0, sticky = W)
        self.vec_1_x = Entry(self)
        self.vec_1_x.grid(row = 1, column = 1, sticky = W)

        Label(self,
              text = "Y:"
              ).grid(row = 2, column = 0, sticky = W)
        self.vec_1_y = Entry(self)
        self.vec_1_y.grid(row = 2, column = 1, sticky = W)

        Label(self,
              text = "Z:"
              ).grid(row = 3, column = 0, sticky = W)
        self.vec_1_z = Entry(self)
        self.vec_1_z.grid(row = 3, column = 1, sticky = W)
        
        
        
        
        
        #####VECTOR 2#####
        Label(self,
              text = "Enter the components of Vector 2:\
              \nNote: The program will only take numbers."
              ).grid(row = 8, column = 0, columnspan = 2, sticky = W)
        Label(self,
              text = "Vector 2:"
              ).grid(row = 20, column = 0, columnspan = 2, sticky = W)

        # create a label and text entry for the name of a person
        Label(self,
              text = "X: "
              ).grid(row = 11, column = 0, sticky = W)
        self.vec_2_x = Entry(self)
        self.vec_2_x.grid(row = 11, column = 1, sticky = W)

        # create a label and text entry for a plural noun
        Label(self,
              text = "Y:"
              ).grid(row = 12, column = 0, sticky = W)
        self.vec_2_y = Entry(self)
        self.vec_2_y.grid(row = 12, column = 1, sticky = W)

        # create a label and text entry for a verb
        Label(self,
              text = "Z:"
              ).grid(row = 13, column = 0, sticky = W)
        self.vec_2_z = Entry(self)
        self.vec_2_z.grid(row = 13, column = 1, sticky = W)
     
        def close_window():
            root.destroy()

        #BUTTON###
        Button(self,
               text = "Click to input Vectors",
               command = self.vector1buttonpress
               ).grid(row = 17, column = 1, sticky = W)
               
        Button(self,
               text = "Click to close program",
               command = close_window).grid(row = 100, column = 1, sticky = W)

               
               ####OUTPUTS####
        self.vector1_info_txt = Text(self, width = 50, height = 1, wrap = WORD)
        self.vector1_info_txt.grid(row = 19, column = 0, columnspan = 4)
        self.vector2_info_txt = Text(self, width = 50, height = 1, wrap = WORD)
        self.vector2_info_txt.grid(row = 21, column = 0, columnspan = 4)
        self.dotproduct_txt = Text(self, width = 75, height = 1, wrap = WORD)
        self.dotproduct_txt.grid(row = 1, column = 75, columnspan = 4)
        self.crossproduct_txt = Text(self, width = 75, height = 1, wrap = WORD)
        self.crossproduct_txt.grid(row = 1, column = 200, columnspan = 4)
        self.vector1mag_txt = Text(self, width = 75, height = 1, wrap = WORD)
        self.vector1mag_txt.grid(row = 5, column = 75, columnspan = 4)
        self.vector2mag_txt = Text(self, width = 75, height = 1, wrap = WORD)
        self.vector2mag_txt.grid(row = 5, column = 200, columnspan = 4)
        self.vector2unit_txt = Text(self, width = 75, height = 1, wrap = WORD)
        self.vector2unit_txt.grid(row = 9, column = 200, columnspan = 4)
        self.vector1unit_txt = Text(self, width = 75, height = 1, wrap = WORD)
        self.vector1unit_txt.grid(row = 9, column = 75, columnspan = 4)
        self.component_1_on_2_txt = Text(self, width = 75, height = 1, wrap = WORD)
        self.component_1_on_2_txt.grid(row = 13, column = 75, columnspan = 4)
        self.component_2_on_1_txt = Text(self, width = 75, height = 1, wrap = WORD)
        self.component_2_on_1_txt.grid(row =13 , column = 200, columnspan = 4)
        self.projection_1_on_2_txt = Text(self, width = 75, height = 1, wrap = WORD)
        self.projection_1_on_2_txt.grid(row = 17, column = 75, columnspan = 4)
        self.projection_2_on_1_txt = Text(self, width = 75, height = 1, wrap = WORD)
        self.projection_2_on_1_txt.grid(row = 17, column = 200, columnspan = 4)
    
    def vector1buttonpress(self):
        """executes the other functions when the button is pressed"""
        self.maths();
        self.tell_vector1_info();
        self.tell_vector2_info();
        self.graph();
    def vector1saved(self):
        x=None        
        x=self.vector1()
        return x
    def vector2saved(self):
        y=None        
        y=self.vector2()
        return y
    def maths(self):
        """updates the math outputs on the display"""
        dot=self.dotproduct(); 
        cross=self.crossproduct();
        mag1=self.magnitude1();
        mag2=self.magnitude2();
        unitvec_1=self.unitvector1()
        unitvec_2=self.unitvector2()
        compvec_1=self.component1()
        compvec_2=self.component2()
        projection1=self.projection1on2()
        projection2=self.projection2on1()
        self.crossproduct_txt.delete(0.0, END)
        self.crossproduct_txt.insert(0.0, cross)
        self.dotproduct_txt.delete(0.0, END)
        self.dotproduct_txt.insert(0.0, dot)
        self.vector1mag_txt.delete(0.0, END)
        self.vector1mag_txt.insert(0.0, mag1);
        self.vector2mag_txt.delete(0.0, END)
        self.vector2mag_txt.insert(0.0, mag2);
        self.vector1unit_txt.delete(0.0, END)
        self.vector1unit_txt.insert(0.0, unitvec_1);
        self.vector2unit_txt.delete(0.0, END)
        self.vector2unit_txt.insert(0.0, unitvec_2);
        self.component_1_on_2_txt.delete(0.0, END)
        self.component_1_on_2_txt.insert(0.0, compvec_1);
        self.component_2_on_1_txt.delete(0.0, END)
        self.component_2_on_1_txt.insert(0.0, compvec_2);
        self.projection_1_on_2_txt.delete(0.0, END)
        self.projection_1_on_2_txt.insert(0.0, projection1);
        self.projection_2_on_1_txt.delete(0.0, END)
        self.projection_2_on_1_txt.insert(0.0, projection2);

    def crossproduct(self):
        """calculates and returns crossproduct"""
        if len(self.vector1())==len(self.vector2()):
            vector1=np.array(self.vector1()) 
            vector2=np.array(self.vector2())
            crossproducttrue=np.cross(vector2,vector1)
            return str(crossproducttrue)
    def dotproduct(self):
        """calculates and returns dotproduct"""
        if len(self.vector1())==len(self.vector2()):
            vector1=np.array(self.vector1()); 
            vector2=np.array(self.vector2());
            dotproducttrue=np.dot(vector2,vector1);
            return str(dotproducttrue);
    def magnitude1(self):
        """calculates and returns magnitude of vector 1"""
        mag1=0        
        for x in range(len(self.vector1())):        
            mag1+=self.vector1()[x]**2
        mag1withsqrt=math.sqrt(mag1);
        return mag1withsqrt;
    def magnitude2(self):   
        """calvulates and returns magnitude of vector 2"""
        mag2=0        
        for x in range(len(self.vector2())):        
            mag2+=self.vector2()[x]**2
        mag2withsqrt=math.sqrt(mag2)
        return mag2withsqrt
    def unitvector1(self):
        """calculates unit vector 1"""
        unitvector1=self.vector1()
        for x in range(len(self.vector1())):
            unitvector1[x]/=self.magnitude1()
        return unitvector1
    def unitvector2(self):
        """calculates unit vector 2"""
        unitvector2=self.vector2()
        for x in range(len(self.vector2())):
            unitvector2[x]/=self.magnitude2()
        return unitvector2
    def component1(self):
        """calculates the component of vector 1 on vector 2"""
        comp1=0     
        for x in range(len(self.vector1())):
            comp1+=self.vector1()[x]*self.unitvector2()[x]
        return comp1
    def component2(self):
        """calculates the component of vector 2 on vector 1"""
        comp2=0     
        for x in range(len(self.vector2())):
            comp2+=self.vector2()[x]*self.unitvector1()[x]
        return comp2
    def projection1on2(self):
        """calculates the projection of vector 1 on vector 2"""
        projection=self.unitvector2();
        for x in range(len(self.unitvector2())):
            projection[x]*=self.component1()
        return projection
    def projection2on1(self):
        """calculates the projection of vector 2 on vector 1"""
        projection=self.unitvector1();
        for x in range(len(self.unitvector1())):
            projection[x]*=self.component2()
        return projection
    def vector2(self):
        """retrieves whatever is currently inputted into vector 2"""
        vector2x=self.vec_2_x.get()
        vector2y= self.vec_2_y.get()
        vector2z = self.vec_2_z.get()
        vector2=[int(vector2x),int(vector2y),int(vector2z)]
        return vector2

    def vector1(self):
        """retrieves whatever is currently inputted into vector 1"""
        vector1x=self.vec_1_x.get()
        vector1y= self.vec_1_y.get()
        vector1z = self.vec_1_z.get()
        vector1=[int(vector1x),int(vector1y),int(vector1z)]
        return vector1

    def tell_vector2_info(self):    
        """this function tells the user what the current vector 2 is"""
        vector2x=self.vector2()[0]
        vector2y= self.vector2()[1]
        vector2z = self.vector2()[2]
        
        vector2_info = "<"
        vector2_info += str(vector2x)
        vector2_info += ","
        vector2_info += str(vector2y)
        vector2_info += ","
        vector2_info += str(vector2z)
        vector2_info += ">"
        self.vector2_info_txt.delete(0.0, END)
        self.vector2_info_txt.insert(0.0, vector2_info)

    def tell_vector1_info(self):
        """ This function tells the user what the current vector 1 is """
       

       # get values from the GUI
        vector1x = self.vector1()[0]
        vector1y= self.vector1()[1]
        vector1z = self.vector1()[2]
        
        

        # create the vector1_info
        vector1_info = "<"
        vector1_info += str(vector1x)
        vector1_info += ","
        vector1_info +=str(vector1y)
        vector1_info += ","
        vector1_info += str(vector1z)
        vector1_info += ">"
        # display the vector1_info                                
        self.vector1_info_txt.delete(0.0, END)
        self.vector1_info_txt.insert(0.0, vector1_info)

 #   def graph(self):
 #       """Graphs vector 1 and vector 2 in threespace, 
 #       then embeds the graph into tkinter"""
 #       f= Figure(figsize=(10,10),dpi=100)
 #       #Attempted following https://www.youtube.com/watch?v=Zw6M-BnAPP0 
 #       vector1=self.vector1();
 #       vector2=self.vector2();
 #       #fig = plt.figure()
 #       ax = plt.figure().add_subplot(111,projection='3d')
 #       
 #       X,Y,Z=[0,vector1[0]],[0,vector1[1]],[0,vector1[2]]
 #       A,B,C=[0,vector2[0]],[0,vector2[1]],[0,vector2[2]]
 #       # put 0s on the y-axis, and put the y axis on the z-axis
 #       ax.plot(X,Y,Z, label='Vector 1')
 #       ax.plot(A,B,C, label='Vector 2')
 #       ax.legend()
 #       ax.set_xlabel("X Axis");
 #       ax.set_ylabel("Y Axis");
 #       ax.set_zlabel("Z Axis");
 #       
 #       canvas=FigureCanvasTkAgg(f,self)
 #       #issues getting graph to show, to be fixed later
 #       canvas.show()
 #       canvas.get_tk_widget().grid(row = 120000, column = 20,sticky=N)
        
 #       toolbar=NavigationToolbar2Tk(canvas,self)
 #       toolbar.update()
 #       canvas.tkcanvas.grid(row = 120000, column = 20,sticky=N)


### main ###
root = Tk.Tk()
root.title("Vector Calculator v1.0")
#in future, make it adapt to screen size
root.geometry("1980x1080")
app = Application(root)
root.mainloop()