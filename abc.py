from collections import defaultdict 


class Graph: 

    def __init__(self): 

        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
 
    def BFS(self, s, avoid): 

        found = [False] * (len(self.graph)) 

        qu = [] 
        link = [-1]*64

        qu.append(s) 
        found[s] = True

        while qu: 

            s = qu.pop(0) 

            for i in self.graph[s]: 
                if i in avoid:
                    continue
                if found[i] == False: 
                    qu.append(i) 
                    found[i] = True
                    link[i] = s

        temp = 63
        traversal = []
        traversal.append(64)
        exist = True
        while True:
            if temp == 0:
                break
            if temp == -1:
                exist = False
                print('can not traverse')
                break
            traversal.append(link[temp]+1)
            temp = link[temp]

        if exist == True:
            print(traversal[::-1])

g = Graph() 
n = 8
for i in range(n):
    for j in range(n):
        if j != 0:
            g.addEdge(i*8+j, i*8+j-1)
        if j != 7:
            g.addEdge(i*8+j, i*8+j+1)
        if i != 0:
            g.addEdge(i*8+j, (i-1)*8+j)
            if j != 0:
                g.addEdge(i*8+j, 8*(i-1)+(j-1))
            if j != 7:
                g.addEdge(i*8+j, 8*(i-1)+(j+1))
        if i != 7:
            g.addEdge(i*8+j, (i+1)*8+j)
            if j != 0:
                g.addEdge(i*8+j, 8*(i+1)+(j-1))
            if j != 7:
                g.addEdge(i*8+j, 8*(i+1)+(j+1))
            

x = input()
y = []
while True:
    if x != 'Y':
        break
    a, b = map(int, input().split())
    c = 8*(a-1)+b-1
    y.append(c)
    g.BFS(0, y)
    choice = input()
