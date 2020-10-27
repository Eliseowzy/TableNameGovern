import networkx as nx

def read_graph():
    file = open('./data/data','r+')
    graph = nx.DiGraph()
    for line in file.readlines():
        edge_data = line.strip('\n').strip('\t').split(' ')
        node_1 = int(edge_data[0])
        node_2 = int(edge_data[1])
        names = edge_data[2:]
        graph.add_edge(node_1,node_2,names = names)
    return graph

