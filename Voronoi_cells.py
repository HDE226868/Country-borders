import numpy as np
import matplotlib.pyplot as plt

P1 = [2,1]
P2 = [9,5]
P3 = [4,7]

Set = [P1,P2,P3]

def dist(point1,point2):
    """Returns distance between two points."""
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def perp(point1,point2):
    """Returns slope and y-intercept of the perpendicular
    bisector of the segment connecting two cities."""
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    """
    try:
        m = (x2 - x1)/(y1 - y2)
        b = x1**2 + y1**2 - x1**2 - y2**2
        return ['yes',m,b]
    except ZeroDivisionError:
        mid = (x2 - x1)/2
        return ['no',mid]
    """
    m = (x2 - x1)/(y1 - y2)
    b = (x1**2 + y1**2 - x2**2 - y2**2)/(2*(y1 - y2))
    return m,b

M1 = perp(P1,P2)[0]
B1 = perp(P1,P2)[1]
M2 = perp(P1,P3)[0]
B2 = perp(P1,P3)[1]

def vertex():
    """Finds central vertex"""
    x = (B1 - B2)/(M2 - M1)
    y = M1*x + B1
    return x,y

"""
This next bit divides each of the lines into a certain number of line
segments by adding a number of points onto the lines, and then removes
those points in the third city's Voronoi cell.
"""
for point1 in Set:
    for point2 in Set:
        if point2 != point1:
            N = []
            delta = 0.001
            for i in range(0,10000):
                N.append(i*delta)
            M = [perp(point1,point2)[0]*a + perp(point1,point2)[1] for a in N]
            Other_point = [a for a in Set if a not in [point1,point2]]
            i = 0
            while i < len(N):
                x = N[i]
                y = M[i]
                if dist([x,y],point1) > dist([x,y],Other_point[0]):
                    N.remove(x)
                    M.remove(y)
                else:
                    i += 1
            plt.plot(N,M,'k')

for point in Set:
    name = 'City at ('+str(point[0])+','+str(point[1])+')'
    plt.plot(point[0],point[1],'x',label=name)

plt.plot(vertex()[0],vertex()[1],'kx')
plt.legend(loc='upper left')
plt.title('Voronoi cells of three countries')
plt.xlim(0,10)
plt.ylim(0,10)
plt.show()
