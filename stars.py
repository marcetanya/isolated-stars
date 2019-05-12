# -*- coding: utf-8 -*-
"""
Code Challenge: Isolated Stars.
(c) CGWA Time Domain Astronomy Group
"""

import math


class Node(object):
    """Represents node in a graph"""

    def __init__(self, name, index, is_iso = True):
        """
        Constructs the self.name and self.is_iso attributes of the class. Note
        self.is_iso is set to True as default.
        """
        self.name = name
        self.index = index
        self.is_iso = is_iso

    def get_name(self):
        """Returns self.name"""
        return self.name
    
    def get_index(self):
        """Returns the index of the tuple in the original list"""
        return self.index
        
    def get_iso(self):
        """Returns self.iso"""
        return self.is_iso

    def change_iso(self):
        """Changes self.iso from True to False"""
        self.is_iso = False
        
    def __eq__(self, other):
        """Checks whether two nodes are the same node"""
        if not isinstance(other, Node):
            other = Node(other)
        return self.name == other.name

    def __ne__(self, other):
        """Checks whether two nodes are distinct"""
        return not self.__eq__(other)

    def __hash__(self):
        # This function is necessary so that Nodes can be used as
        # keys in a dictionary, even though Nodes are mutable
        return self.name.__hash__()

    def __str__(self):
        """Returns name of node in string format"""
        return str(self.name)


class WeightedEdge(object):
    """Represents an edge in the graph"""
    
    def __init__(self, src, dest, dist):
        """Represents an edge in the graph"""
        self.src = src
        self.dest = dest
        self.dist = dist
        
    def get_src(self):
        """Returns self.src"""
        return self.src
    
    def get_dest(self):
        """Returns self.dest"""
        return self.dest
    
    def get_dist(self):
        """Returns the distance between two nodes"""
        return self.dist
    
    def __str__(self):
        """Returns a formatted string which represents the edge"""
        return '{0}<->{1} ({2})'.format(self.src, self.dest, self.dist)


class Graph(object):
    """Represents graph of Node and Edge objects"""
    
    def __init__(self):
        """Constructs the self.nodes and self.edges attributes of the class"""
        self.nodes = set()
        self.edges = {}

    def __str__(self):
        """Returns the edges of a graph as a list, with one edge per line"""
        edge_strs = []
        
        for edges in self.edges.values():
            for edge in edges:
                edge_strs.append(str(edge))
                
        edge_strs = sorted(edge_strs)
        return '\n'.join(edge_strs)
    
    def get_edges(self, node):
        """Returns self.edges[node]"""
        return self.edges[node]
    
    def has_node(self, node):
        """Returns boolen, True if graph contains specified node"""
        return node in self.nodes
    
    def add_node(self, node, index):
        """Adds node to graph, raises ValueError if duplicate"""
        if not isinstance(node, Node):
            node = Node(node, index)
            
        if node in self.nodes:
            raise ValueError('Duplicate node')
            
        else:
            self.nodes.add(node)
            self.edges[node] = []
    
    def add_edge(self, edge):
        """Adds edge to graph, raises ValueError if either node not in graph"""
        source = edge.get_src()
        destination = edge.get_dest()
        total_distance = edge.get_dist()
        
        if source not in self.nodes:
            raise ValueError("Source node not in graph")
        
        elif destination not in self.nodes:
            raise ValueError("Destination node not in graph")
        
        elif source in self.nodes and destination in self.nodes:
            self.edges[source].append(WeightedEdge(source, destination,
                                                   total_distance))


def calculate_dist(node_a, node_b):
    """Returns distance between two objects at coordinate pairs a and b"""
    node_a = node_a.get_name()
    node_b = node_b.get_name()

    x1, y1 = int(node_a[0]), int(node_a[1])
    x2, y2 = int(node_b[0]), int(node_b[1])    
    
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def load_graph(list, iso_distance):
    """
    Loads a map from a given list of tuples, with edges denoting distances
    between nodes.
    """
    graph = Graph()
    
    for index, tuple in enumerate(list):
        new_node = Node(tuple, index)
        graph.add_node(new_node, index)
        
        for old_node in graph.nodes:
            
            if old_node.__ne__(new_node):
                source = new_node
                destination = old_node
                distance = calculate_dist(source, destination)
    
                graph.add_edge(WeightedEdge(source, destination, distance))
                
                if new_node.get_iso() is True:
                    if distance < iso_distance:
                        new_node.change_iso()
                        old_node.change_iso()
    
    return graph
        
    
def isolated(star_list, dist_min):
    """
    Given a list of (x, y) pair tuples representing star positions on an image,
    return a list with the indices of the isolated stars.
    Isolated stars are stars that are at least farther than `dist_min` from any other
    star.
    Return list may be empty if no stars are isolated.
    """
    isolated_graph = load_graph(star_list, dist_min)
    isolated_stars = []
    
    for node in isolated_graph.nodes:
        if node.get_iso() is True:
            isolated_stars.append(node.index)
    
    return isolated_stars