# Catch-the-thief-game-
here we have attempted to make a computer version of the board game scotland yard. A random graph is created and positions are assigned on the graph for the police and the thief. Police here is the user and thief is always the computer.The rules of the game will be explained once the project is completed.




#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HARSHIL NORI,MIHIR RAVITEJ,KAVIN P
#
# Created:     25-04-2015
# Copyright:   (c) HARSHIL NORI 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt
import numpy
import time
from random import randint

#For check function condition
def doNothing():
    print("ok ok I won't...")

#networkx components
def play():
    d={}
    g=nx.Graph(d)
    l=[None,None]
    def drawgraph():
        a=[[ 0, 0, 0, 0,  1, 0,  1,  1,  1,  0],
        [ 0,  0,  0,  1,  1,  1,  1,  1,  0,  0],
        [ 0,  0,  0,  1,  0,  0,  0,  0,  0,  0],
        [ 0,  1,  1,  0,  1,  1,  1,  0,  1,  0],
        [ 1,  1,  0,  1,  0,  1,  0,  0,  0,  0],
        [ 0,  1,  0,  1,  1,  0,  0,  1,  0,  1],
        [ 1,  1,  0,  1,  0,  0,  0,  0,  0,  0],
        [ 1,  1,  0,  0,  0,  1,  0,  0,  0,  1],
        [ 1,  0,  0,  1,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  1,  0,  1,  0,  0]]
        d={}
        g=nx.Graph()
        for i in range(0,10):
            for j in range(0,10):
                if(g.has_node(j)==True):
                    if((g.has_edge(i,j) or g.has_edge(j,i))!=True):
                        if(a[i][j]==1):
                            g.add_edge(i,j)
                else:
                    g.add_node(j)
        nx.draw(g)
        plt.savefig("p.png",format="PNG")
        plt.show(block=False)
        time.sleep(5)
        plt.close()
        return g
    def updatel(l):
        mapping={}
        while(1):
            x=randint(1,10)
            if(x in g):
                mapping[x]='thief'
                break
        while(1):
            y=randint(1,9)
            if(y in g and y!=x):
                mapping[y]='police'
                break
        l=[x,y]
        return l
    def init_mappingnode(g,l):
        mapping={}
        while(1):
            x=l[0]
            if(x in g):
                mapping[x]="thief"
                break
        while(1):
            y=l[1]
            if(y in g):
                mapping[y]="police"
                break
        g=nx.relabel_nodes(g,mapping)
        nx.draw(g)
        plt.savefig("p.png",format="PNG")
        plt.show(block=False)
        l=[x,y]
        time.sleep(5)
        return g
    def map_nodepolice(i,l,g):
        mapping={}
        while(True):
            if(i!='thief'):
                i=int(i)
            if(g.has_edge('police',i) or g.has_edge(i,'police')):
                mapping['police']=l[1]
                l[1]=i
                mapping[i]='police'
                g=nx.relabel_nodes(g,mapping)
                #nx.draw(g)
                #plt.savefig("p.png",format="PNG")
                #plt.show(block=False)
                #time.sleep(5)
                break
            else:
                #print("not a valid input as there is no edge")
                #root1 = Tk()
                #label = Label(root1,text = 'Wrong\Invalid input')
                #label.pack()
                #root1.mainloop()
                #time.sleep(2)
                print("wrong/invalid input as the node is not connected")

                nx.draw(g)
                plt.savefig("p.png",format="PNG")
                plt.show(block=False)
                time.sleep(5)
                plt.close()
                i=input("enter a valid node to to move to")
        return g
    def map_nodethief(g,l):
        mapping={}
        temp=nx.shortest_path(g,'thief','police')
        n=len(temp)
        moveto=l[0]
        moved=0
        for i in g['thief']:
            temp=nx.shortest_path(g,i,'police')
            length=len(temp)
            if(length>=n):
                n=length
                moveto=i
                moved=1
        if(moved==1):
            mapping['thief']=l[0]
            l[0]=moveto
            mapping[moveto]='thief'
            g=nx.relabel_nodes(g,mapping)
        return g
    g=nx.Graph()
    g=drawgraph()
    l=updatel(l)
    counter=0
    print (l)
    g=init_mappingnode(g,l)
    plt.close()
    while(True):
        i=input("enter the node to move to")
        g=map_nodepolice(i,l,g)
        counter=counter+1
        if(i!='thief'):
            l[1]=int (i)
        else:
            l[1]=i
        print(l)
        if(l[1]=='thief'):
            check='won'
            print('won')
            break
        elif(counter==10):
            check ='lost'
            print("lost")
            break
        g=map_nodethief(g,l)
        nx.draw(g)
        plt.savefig("p.png",format="PNG")
        plt.show(block=False)
        time.sleep(5)
        plt.close()
        if(counter%1==0):
            nx.draw(g)
            plt.savefig("p.png",format="PNG")
            plt.show(block=False)
            time.sleep(5)
            plt.close()
    print(counter)

#Dijkstra algorithm
import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return


root = Tk()
root.geometry("700x600+250+250")

var = StringVar()
label1 = Label( root, textvariable=var,fg = 'black',font=("Helvetica", 20), anchor=W)
var.set("Scotland Yard")
label1.pack()
background_image=PhotoImage(file="C:\\Users\\HARSHIL NORI\\Desktop\\scotland1.gif")
background_label = Label(root, image=background_image)

background_label.place(x=0, y=40, relwidth=1, relheight=1)
# Tkinter puts menus at the top by default
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
# Adds a drop down when "File" is clicked
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Game", command=play)
subMenu.add_command(label="High Scores", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Restart", command=play)

# ******* Creating a Toolbar *******

toolbar = Frame(root, bg="blue")

toolbar.pack(side=TOP, fill=X)

# ******* Creating a Status Bar for the Bottom *******

# bd is border, relief is type of border
status = Label(root, text="Preparing to start game", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
