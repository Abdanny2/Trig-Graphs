import numpy as np
import math as m
from matplotlib import pyplot as plt


pi=round(m.pi,3)

x=np.arange(0,10, 0.001)
A=1.0
C=2*pi
B=0.0
D=0.0


def sine(A,B,C,D):
    
    y=A*(np.sin((2*pi*(x-B))/C))+ D

    plt.plot(x,y) #plot the graph of y function of x
    plt.axhline(y=0, color='k')  #plot the x axis
    plt.axvline(x=0, color='k') #plot the y axis
    plt.grid(True)          #plot the gridlines
    plt.xlabel('x')   #label the x axis
    plt.ylabel('sin(x)')        #label the y axis

    plt.show()
    return;     



def cosine(A,B,C,D):
    
    y=A*(np.cos((2*pi*(x-B))/C))+ D

    plt.plot(x,y) #plot the graph of y function of x
    plt.axhline(y=0, color='k')  #plot the x axis
    plt.axvline(x=0, color='k') #plot the y axis
    plt.grid(True)          #plot the gridlines
    plt.xlabel('x')   #label the x axis
    plt.ylabel('cos(x)')        #label the y axis

    plt.show()
    return;


print("\n\t\t Sine and Cosine Trigonometry graph calculator!")
print("\t","-"*55)


end_program = 1


while end_program:
    c=int(input("Press 1 for sine or 0 for cosine: "))
    if c==1:
        print("You chose to graph the function sine, the form:")
        print("f(x)=A*sin((2*pi*(x-B))/C))+ D")
        print("Enter the graph properties when prompted:")
        A=float(input("Amplitude (A)= "))
        B=float(input("Phase shift (B)= "))
        C=float(input("Period (can't be 0)(C)= "))
        D=float(input("Vertical shift (D)= "))
        sine(A,B,C,D)
        end_program=int(input("Do you want to do another graph? Press 1 for Yes and 0 for No \n"))
  

    elif c==0:
        print("You chose to graph the function cosine, the form:")
        print("f(x)=A*cos((2*pi*(x-B))/C))+ D")
        print("Enter the graph properties when prompted:")
        A=float(input("Amplitude (A)= "))
        B=float(input("Phase shift (B)= "))
        C=float(input("Period (can't be 0)(C)= "))
        D=float(input("Vertical shift (D)= "))
        cosine(A,B,C,D)
        end_program=int(input("Do you want to do another graph? Press 1 for Yes and 0 for No\n"))
        
    else:
        print("Oops Wrong choice!!")
        continue
            
    

        
