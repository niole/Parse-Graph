import collections

def parseGraphFromString(inputLines):
    graph = collections.defaultdict(set)
    for line in inputLines:
        graph[line[0]].add(line[5])
    return graph

output = {
        'a' : {'b', 'c'},
        'b' : {'c', 'f'},
        'd' : {'a'}
        }
inputLines = """a -> b
b -> c
a -> c
d -> a
b -> f""".split('\n')

def iterFindNextNode(g,target,start,currNode,i,visited):
    """
    Looks for next unvisited child node in g[currNode] and
    calls main function on it.
    If no unvisited nodes, function calls iterBackTrack,
    to find previous node with unvisited children.
    """
    if len(g[currNode]) > 0 and i != len(g[currNode]):
        if g[currNode][i] not in visited:
            return iterBfsGraph(g,target,start,g[currNode][i],visited)
        else:
            return iterFindNextNode(g,target,start,currNode,i+1,visited)
    if i == len(g[currNode]):
        return

def childrenVisited(g,start,parent,visited):
    children = [x for x in g[parent] if x in visited]
    if len(children) == len(g[parent]):
        return True
    return False

def iterBackTrack(g,target,start,currNode,visited):
    for parent in visited:
        if parent == start and childrenVisited(g,start,parent,visited):
            print "Can't reach target node."
            return
        if currNode in g[parent]:
            return iterBfsGraph(g,target,start,parent,visited)

def iterBfsGraph(g,target,start,currNode,visited):
    """
    Continue search until path matches one in visited.
    Continue until can't go forward and save visited nodes.
    Back track until find node with path not in visited.
    Assume all targets accessible and no loops exist.

    """
    while currNode != target:
        if currNode in visited and iterFindNextNode(g,target,start,currNode,1,visited) != False:
            #for backtracking: if current parent already in visited, but not all of it's children have
            #been searched
            return iterFindNextNode(g,target,start,currNode,0,visited)
        if currNode not in visited:
            #if current node not visited and therefore none of its children visited, first check if has children,
            #if has children call iterFindNextNode
            visited.add(currNode)
            if currNode in g:
                return iterFindNextNode(g,target,start,currNode,0,visited)
            else:
                return iterBackTrack(g,target,start,currNode,visited)
        else:
            #if current node and all of it's children in visited, backtrack to previous parent node
            return iterBackTrack(g,target,start,currNode,visited)
    print currNode
# --------------------------------------------#
graph = dict(parseGraphFromString(inputLines))
def convertGraph(graph):
    for e in graph:
        graph[e] = list(graph[e])
    return graph
#print convertGraph(graph)
# -------------------------------------------#
print iterBfsGraph(convertGraph(graph),'f','a','a',set())
