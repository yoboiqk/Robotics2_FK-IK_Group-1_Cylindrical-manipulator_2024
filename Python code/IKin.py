import numpy as np

#link lengths in mm
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))

#Position Vector in mm
xe = float(input("X = "))
ye = float(input("Y = "))
ze = float(input("Z = "))

#Inverse Kinematics Solution using Graphical Method

#Solve for Theta 1
T1 = np.arctan(ye/xe)
T1 = T1*180.0/np.pi

#Solve for d2
d2 = ze - a1 - a2

#Solve for d3
d3 = np.sqrt(ye**2+xe**2) - a3

#Print joint variables
print("Th1 = ", np.around(T1,3))
print("d2 = ", np.around(d2, 3))
print("d3 = ", np.around(d3, 3))