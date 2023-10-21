from DSALinkedList import DSALinkedList
from DSAGraphNode import DSAGraphNode
from DSAQueue import DSAQueue
from DSAStack import DSAStack
import csv


class DSAGraph:
    def __init__(self):
        self.vertices = DSALinkedList()

    def add_vertex(self, shopNumber, value, category, location, rating):
        new_vertex = DSAGraphNode(shopNumber, value, category, location, rating)
        self.vertices.insert_last(new_vertex)
        return new_vertex

    def delete_vertex(self, shopNumber):
        vertex_to_delete = self.get_vertex(shopNumber)
        if vertex_to_delete is None:
            raise ValueError(f"Vertex with shopNumber {shopNumber} not found!")
        for vertex in self.vertices:
            for adjacent_vertex in vertex.get_adjacent():
                if adjacent_vertex.get_shopNumber() == vertex_to_delete.get_shopNumber():
                    vertex.delete_edge(vertex_to_delete)
        self.vertices.remove_node(vertex_to_delete)

    def delete_edge(self, shopNumber_one, shopNumber_two):
        vertex_one = self.get_vertex(shopNumber_one)
        vertex_two = self.get_vertex(shopNumber_two)
        vertex_one.delete_edge(vertex_two)
        vertex_two.delete_edge(vertex_one)

    def add_edge(self, shopNumber_one, shopNumber_two):
        vertex_one = self.get_vertex(shopNumber_one)
        vertex_two = self.get_vertex(shopNumber_two)
        vertex_one.add_edge(vertex_two)
        vertex_two.add_edge(vertex_one)

    def has_vertex(self, shopNumber):
        return self.vertices.contains(shopNumber)

    def get_vertex_count(self):
        return self.vertices.size()

    def get_edge_count(self):
        count = 0
        for vertex in self.vertices:
            count += len(vertex.get_adjacent())
        return count // 2

    def get_vertex(self, shopNumber):
        x = None
        for node in self.vertices:
            vertex = node
            if vertex.get_shopNumber() == shopNumber:
                x = vertex
        
        return x


    def get_adjacent(self, shopNumber):
        vertex = self.get_vertex(shopNumber)
        if vertex:
            connected_nodes = vertex.get_adjacent()
        else:
            raise ValueError("The vertex doesn't exist")
        return connected_nodes

    def is_adjacent(self, shopNumber_one, shopNumber_two):
        vertex_one = self.get_vertex(shopNumber_one)
        vertex_two = self.get_vertex(shopNumber_two)
        return vertex_two in vertex_one.get_adjacent() if vertex_one and vertex_two else False

    def display_as_list(self):
        for vertex in self.vertices:
            adjacent_shopNumbers = [node.get_shopNumber() for node in vertex.get_adjacent()]
            print(vertex.get_shopNumber(), "->", adjacent_shopNumbers)

    def display_as_matrix(self):
        labels = [vertex.get_shopNumber() for vertex in self.vertices]
        matrix = [[0 for _ in labels] for _ in labels]
        for i, vertex_one in enumerate(self.vertices):
            for j, vertex_two in enumerate(self.vertices):
                matrix[i][j] = 1 if vertex_two in vertex_one.get_adjacent() else 0

    def import_shops_from_csv(filename, graph, shop_table):
        with open(filename, mode='r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            next(csv_reader)  # skip header row
            
            for row in csv_reader:
                shopNumber, shopName, category, location, rating = row

                # Add vertex to graph
                shop_info = graph.add_vertex(shopName, shopNumber, category, location, int(rating))

                # Add shop info to hash table
                shop_table.put_item(shopNumber, shop_info)


    


    # def breadth_first_search(self, start_label, end_label):
    #     q = DSAQueue()

    #     for vertex in self.vertices:
    #         vertex.clear_visited()
    #         vertex.predecessor = None

    #     start_vertex = self._find_vertex(start_label)
    #     end_vertex = self._find_vertex(end_label)

    #     if not start_vertex or not end_vertex:
    #         print("Start or end vertex not found!")
    #         return

    #     start_vertex.set_visited()
    #     q.enqueue(start_vertex)

    #     path_found = False

    #     while not q.is_empty():
    #         current_vertex = q.dequeue()

    #         if current_vertex == end_vertex:
    #             path_found = True
    #             break

    #         for w in current_vertex.get_adjacent():
    #             if not w.get_visited():
    #                 w.set_visited()
    #                 w.predecessor = current_vertex
    #                 q.enqueue(w)

    #     if path_found:
    #         path = []
    #         at = end_vertex
    #         while at:
    #             path.append(at.label)
    #             at = at.predecessor
    #         path.reverse()
    #         print(" -> ".join(path))
    #     else:
    #         print(f"No path found between {start_label} and {end_label}")


    def breadth_first_search(self, start_label, end_label):
        # Validate the start and end labels before proceeding
        
        start_exists = self.get_vertex(start_label)
        end_exists = self.get_vertex(end_label)

        if not start_exists and not end_exists:
            print("Both start and end shops don't exist!")
            return
        elif not start_exists:
            print("Start shop doesn't exist!")
            return
        elif not end_exists:
            print("End shop doesn't exist!")
            return


        q = DSAQueue()

        # setting visited to false on all vertices
        for vertex in self.vertices:
            vertex.clear_visited()

        start_vertex = self.get_vertex(start_label)
        end_vertex = self.get_vertex(end_label)

        start_vertex.set_visited()
        q.enqueue(start_vertex)

        path_found = False

        while not q.is_empty():
            current_vertex = q.dequeue()

            if current_vertex == end_vertex:
                path_found = True
                break

            for w in current_vertex.get_adjacent():
                if not w.get_visited():
                    w.set_visited()
                    q.enqueue(w)

        if path_found:
            print(f"Path found between {start_label} and {end_label}")
        else:
            print(f"No path found between {start_label} and {end_label}")





    def depth_first_search(self, start_label, end_label):
        s = DSAStack()

        for vertex in self.vertices:
            vertex.clear_visited()

        start_vertex = self._find_vertex(start_label)
        end_vertex = self._find_vertex(end_label)

        if start_vertex is None or end_vertex is None:
            print("Start or end vertex not found!")
            return

        start_vertex.set_visited()
        s.push(start_vertex)

        path_found = False

        while not s.is_empty():
            current_vertex = s.pop()

            if current_vertex == end_vertex:
                path_found = True
                break

            for w in current_vertex.get_adjacent():
                if not w.get_visited():
                    w.set_visited()
                    s.push(w)

        if path_found:
            print(f"Path found between {start_label} and {end_label}")
        else:
            print(f"No path found between {start_label} and {end_label}")

