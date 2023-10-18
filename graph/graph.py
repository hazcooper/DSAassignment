class DSAGraphNode:
    def __init__(self, label, value=None):
        self.label = label
        self.value = value
        self.adjacent = []
        self.visited = False

    def add_adjacent(self, node):
        if node not in self.adjacent:
            self.adjacent.append(node)

    def clear_visited(self):
        self.visited = False

class DSAGraph:
    def __init__(self):
        self.vertices = []

    def _find_vertex(self, label):
        for vertex in self.vertices:
            if vertex.label == label:
                return vertex
        return None

    def add_vertex(self, label, value=None):
        if not self._find_vertex(label):
            new_vertex = DSAGraphNode(label, value)
            self.vertices.append(new_vertex)
    
    def delete_vertex(self, label):
        node_to_remove = self._find_vertex(label)
        if node_to_remove:
            self.vertices.remove(node_to_remove)
            for node in self.vertices:
                if node_to_remove in node.adjacent:
                    node.adjacent.remove(node_to_remove)

    def add_edge(self, label1, label2):
        node1 = self._find_vertex(label1)
        node2 = self._find_vertex(label2)
        
        if not node1:
            node1 = DSAGraphNode(label1)
            self.vertices.append(node1)
            
        if not node2:
            node2 = DSAGraphNode(label2)
            self.vertices.append(node2)

        node1.add_adjacent(node2)
        node2.add_adjacent(node1)  # For undirected graph

    def delete_edge(self, label1, label2):
        node1 = self._find_vertex(label1)
        node2 = self._find_vertex(label2)

        if node1 and node2:
            if node2 in node1.adjacent:
                node1.adjacent.remove(node2)
            if node1 in node2.adjacent:
                node2.adjacent.remove(node1)

    def _clear_all_visited(self):
        for vertex in self.vertices:
            vertex.clear_visited()

    def breadth_first_search(self, start_label):
        self._clear_all_visited()
        start_vertex = self._find_vertex(start_label)

        if start_vertex is None:
            print("Start vertex not found!")
            return

        queue = [start_vertex]
        start_vertex.visited = True

        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex.label, end=" ")

            for neighbor in current_vertex.adjacent:
                if not neighbor.visited:
                    queue.append(neighbor)
                    neighbor.visited = True

    def depth_first_search(self, start_label):
        self._clear_all_visited()
        start_vertex = self._find_vertex(start_label)

        if start_vertex is None:
            print("Start vertex not found!")
            return

        stack = [start_vertex]
        start_vertex.visited = True

        while stack:
            current_vertex = stack[-1]
            print(current_vertex.label, end=" ")

            unvisited_found = False
            for neighbor in current_vertex.adjacent:
                if not neighbor.visited:
                    stack.append(neighbor)
                    neighbor.visited = True
                    unvisited_found = True
                    break

            if not unvisited_found:
                stack.pop()

    def displayAsList(self):
        for vertex in self.vertices:
            adjacent_labels = [adj.label for adj in vertex.adjacent]
            print(f"{vertex.label} ->", ', '.join(adjacent_labels))

    def displayAsMatrix(self):
        n = len(self.vertices)
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        # Create a mapping from label to index for quick lookup
        label_to_index = {vertex.label: index for index, vertex in enumerate(self.vertices)}

        for vertex in self.vertices:
            for adj_vertex in vertex.adjacent:
                i = label_to_index[vertex.label]
                j = label_to_index[adj_vertex.label]
                matrix[i][j] = 1

        # Displaying the matrix
        header = " ".join([vertex.label for vertex in self.vertices])
        print(" ", header)
        for i in range(n):
            print(self.vertices[i].label, ' '.join(map(str, matrix[i])))

def interactive_menu(graph):
    while True:
        print("\nInteractive Menu:")
        print("a) Add node")
        print("b) Delete node")
        print("c) Add edge")
        print("d) Delete edge")
        print("e) displayAsList")
        print("f) displayAsMatrix")
        print("g) Breadth First Search")
        print("h) Depth First Search")
        print("i) Exit")
        choice = input("Enter your choice: ").lower()

        if choice == 'a':
            label = input("Enter the label of the node: ")
            graph.add_vertex(label)
        elif choice == 'b':
            label = input("Enter node label to delete: ")
            graph.delete_vertex(label)
            pass
        elif choice == 'c':
            label1 = input("Enter the label of the first node: ")
            label2 = input("Enter the label of the second node: ")
            graph.add_edge(label1, label2)
        elif choice == 'd':
            label1 = input("Enter first node label of the edge to delete: ")
            label2 = input("Enter second node label of the edge to delete: ")
            graph.delete_edge(label1, label2)
            pass
        elif choice == 'e':
            print("Displaying graph as a list:")
            graph.displayAsList()
        elif choice == 'f':
            print("Displaying graph as a matrix:")
            graph.displayAsMatrix()
        elif choice == 'g':
            label = input("Enter the starting label for BFS: ")
            graph.breadth_first_search(label)
        elif choice == 'h':
            label = input("Enter the starting label for DFS: ")
            graph.depth_first_search(label)
        elif choice == 'i':
            break
        else:
            print("Invalid choice. Please try again.")
        
    

if __name__ == "__main__":
    graph = DSAGraph()
    interactive_menu(graph)


