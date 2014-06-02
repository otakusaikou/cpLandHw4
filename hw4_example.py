#!/usr/bin/python2.7
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
debug = False

#This function can read data from file
def readData(filename):
    fin = open(filename, "r")
    
    #Read all the lines to a list
    lines = fin.readlines()
    
    #Create empty lists for point name, x and y
    pname = []
    x = []
    y = []
    
    #Store data to lists
    for line in lines:
        pname.append(line.split()[0])
        x.append(float(line.split()[1]))
        y.append(float(line.split()[2]))
        
    return pname, x, y

#This function can calculate area of points with three lists, pname, x and y
def getArea(pname, x, y):
    Area = 0
    #Num is number of points
    num = len(pname)
    for i in range(num):
        Area += (x[i % num] * y[(i + 1) % num]) - (y[i % num] * x[(i + 1) % num]) #Calculate polygon area with formula: ((X1Y2 - Y1X2) + (X2Y3 - Y2X3)+...(XxY1-YyX1)) / 2 = polygon's area.
    return 1.0 * abs(Area) / 2
    
#This function can calculate every length of polygon
def getLength(pname, x, y):
    #variable num is number of points
    num = len(pname)
    _from = []
    _to = []
    length = []
    for i in range(num):
        _from.append(pname[i % num])
        _to.append(pname[(i + 1) % num])
        length.append(math.sqrt((x[i % num] - x[(i + 1) % num])**2 + (y[i % num] - y[(i + 1) % num])**2))
    return _from, _to, length

#This function can write out result
def writeReport(pname, x, y, filename):
    #Open output file, *.out
    fout = open("Result.txt", "w")
    
    #Num is number of points
    num = len(pname)
    
    #Writeout input points
    print "Point-ID   X" + " "*len("%.2f" % x[0]) + "Y\n-----------------------"
    fout.write("Point-ID   X" + " "*len("%.2f" % x[0]) + "Y\n-----------------------\n")
    
    for i in range(num):
        print "%-10s %-.2f %-.2f" % (pname[i], x[i], y[i])
        fout.write("%-10s %-.2f %-.2f\n" % (pname[i], x[i], y[i]))
    
    print "-----------------------"
    fout.write("-----------------------\n")
    
    #Pring length of polygon
    _from, _to, length = getLength(pname, x, y)
    print "From       TO" + " "*(14 - len("%.3f" % length[i])) + "Length\n====================="
    fout.write("From       TO" + " "*(14 - len("%.3f" % length[i])) + "Length\n=====================\n")
    for i in range(num):
        print "%-10s %-10s %-.3f" % (_from[i], _to[i], length[i])
        fout.write("%-10s %-10s %-.3f\n" % (_from[i], _to[i], length[i]))
        
    print "====================="
    fout.write("=====================\n")
        
    print "Perimeter: %.3f" % sum(length)
    print "Area: %.3f" % getArea(pname, x, y)
    print "Xmin: %.2f" % min(x)
    print "Xmax: %.2f" % max(x)
    print "Ymin: %.2f" % min(y)
    print "Ymax: %.2f" % max(y)
    
    fout.write("Perimeter: %.3f\n" % sum(length))
    fout.write("Area: %.3f\n" % getArea(pname, x, y))
    fout.write("Xmin: %.2f\n" % min(x))
    fout.write("Xmax: %.2f\n" % max(x))
    fout.write("Ymin: %.2f\n" % min(y))
    fout.write("Ymax: %.2f\n" % max(y))
    
    fout.close()
    
#This function can plot the result
def plotPolygon(x, y):
    #Connect last point to first point
    x.append(x[0])
    y.append(y[0])

    #Initialize plot
    fig = plt.figure("Polygon")
    ax = fig.add_subplot(111)
    ax.set_title("Result", size = 20)
    ax.plot(x, y, 'b-')
    
    #Alter view range
    plt.xlim([min(x) - 2, max(x) + 2])
    plt.ylim([min(y) - 2, max(y) + 2])

    #Make x, y axis equal scale
    ax.axis('equal')

    #Disable scientific notation
    formatter = ScalarFormatter(useOffset = False)
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)


    #Set axis labels
    plt.xlabel("x")
    plt.ylabel("y")

    #Use grid
    plt.grid()
    plt.show()
    

if __name__ == "__main__":
    if debug:
        filename = "data.txt"
    else:
        filename = raw_input("Input file name:\n")
    pname, x, y = readData(filename)
    #print getArea(pname, x, y)
    #print getLength(pname, x, y)

    writeReport(pname, x, y, filename)
    plotPolygon(x, y)
