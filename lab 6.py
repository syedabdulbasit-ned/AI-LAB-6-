class IDS_SEARCH:
    def __init__(self, num_nodes):
        self.graph = [[] for _ in range(num_nodes)]

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dls(self, node, target, limit):
        print(f"Visiting Node: {node}, Depth Limit: {limit}")
        if node == target:
            return True
        if limit <= 0:
            return False
        for neighbor in self.graph[node]:
            if self.dls(neighbor, target, limit - 1):
                return True
        return False
    def ids(self, start, target, max_depth):
        for depth in range(max_depth + 1):
            print(f"\nStarting new iteration with depth limit: {depth}")
            if self.dls(start, target, depth):
                return True
        return False

num_nodes = 11  

g = IDS_SEARCH(num_nodes)

# Add edges to the graph (directed graph)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)
g.add_edge(3, 7)
g.add_edge(4, 8)
g.add_edge(5, 9)
g.add_edge(6, 10)

start_node = 0
target_node = 9
max_depth = 4

if g.ids(start_node, target_node, max_depth):
    print(f"\nTarget {target_node} found within depth {max_depth}.")
else:
    print(f"\nTarget {target_node} not found within depth {max_depth}.")
