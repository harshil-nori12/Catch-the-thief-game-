# Catch-the-thief-game-
here we have attempted to make a computer version of the board game scotland yard. A random graph is created and positions are assigned on the graph for the police and the thief. Police here is the user and thief is always the computer.The rules of the game will be explained once the project is completed.
import networkx as nx
import matplotlib.pyplot as plt
import numpy
import time
from random import randint
g=nx.barabasi_albert_graph(10,3)
mapping={}
while(1):
    x=randint(1,10)
    if(x in g):
        mapping[x]='thief'
        break
while(1):
    y=randint(1,10)
    if(y in g):
        mapping[y]='police'
        break
H=nx.relabel_nodes(g,mapping)
nx.draw(H)
plt.ion()
n=input("enter the node to move to")
if(H.has_edge('thief',n)):
    mapping['thief']=x
    x=n
    mapping[n]='thief'
else:
    print("no bro! what are u doing macha!")
x=nx.shortest_path(H,'thief','police')
print(x)
plt.savefig("simple_path.png")
plt.show(block=False)
time.sleep(2)
print("hello")
mapping[1]="random"
plt.show()




