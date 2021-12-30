def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class Node:

    # Initializes the info , excite and the adjacency list of the node
    def init(self, excite : float, info:Dict):

        # Is a dictionary that contains information like "name", "type", etc
        self.info : Dict = info

        # Excite is simply a float of the node
        self.excite : float = excite

        # Each element in this list is a tuple of Node and its frequency of firing together
        self.adj_list : List[(Node, int)] = []


    # Inserts a new node and 0 frequency into the list
    def insert_node(self, n):
        self.adj_list.append((n, 0))

    # Calculate the excite by adding the excites of adjacent nodes wieghed by their frequency
    def calculate_excite(self):
        for n, f in self.adj_list:
            self.excite += n.excite * f

        # squish the resulting excite
        self.excite = sigmoid(self.excite)

        # If the nodes fired together, increase their weights/ frequency
        if self.is_active(self.excite) :
            for i in range(len(self.adj_list)):
                if self.is_active(self.adj_list[i][0]): 
                    self.adj_lsit[i][1]+=1

    # Condition for checking whether the excite is sufficient for the node to "fire"
    def is_active(self, n):
        if(n.excite>0.5):
            return True
        return False
