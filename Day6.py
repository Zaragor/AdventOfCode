
class Node:

    def __init__(self, key):
        self.parent = None
        self.key = key
        self.children = list([])

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
    
    def add_parent(self, parent):
        self.parent = parent
        parent.children.append(self)

    def find_distance(self):
        if self.key == 'COM':
            return 0
        if self.parent is None:
            raise Exception('Key:' + self.key + ' has no parent')
        return self.parent.find_distance() + 1
    
    def find_parents(self):
        if self.parent is None:
            return [self.key]
        
        return self.parent.find_parents() + [self.key]

def build_nodes(file_name):
    nodes = list([])
    with open(file_name, "r") as f:
        orbit = f.readline().rstrip('\n')
        while orbit:
            involved_nodes = orbit.split(')')

            if (involved_nodes[1] == 'YQ2'):
                foo = 'bar'
            node_keys = list(map(lambda node: node.key, nodes))
            if involved_nodes[0] in node_keys:
                child = next((node for node in nodes if node.key == involved_nodes[1]), None)
                if child is None:
                    child = Node(involved_nodes[1])
                    nodes.append(child)
                parent = next((node for node in nodes if node.key == involved_nodes[0]), None)
                child.add_parent(parent)
            elif involved_nodes[1] in node_keys:
                parent = next((node for node in nodes if node.key == involved_nodes[0]), None)
                if parent is None:
                    parent = Node(involved_nodes[0])
                    nodes.append(parent)
                child = next((node for node in nodes if node.key == involved_nodes[1]), None)
                parent.add_child(child)
            else:
                parent = Node(involved_nodes[0])
                child = Node(involved_nodes[1])
                nodes.append(parent)
                parent.add_child(child)
                nodes.append(child)
            orbit = f.readline().rstrip('\n')
    
    return nodes

if __name__ == "__main__":

    nodes = build_nodes("day_6_input.txt")
    #print(sum(map(lambda node: node.find_distance(), nodes)))

    santa_node = next((x for x in nodes if x.key == 'SAN'))
    my_node =  next((x for x in nodes if x.key == 'YOU'))

    santa_path = santa_node.find_parents()
    my_path = my_node.find_parents()
    print(santa_path)
    print(my_path)
    index = 0
    for santa_parent in reversed(santa_path):
        if santa_parent in reversed(my_path):
            my_distance = list(reversed(my_path)).index(santa_parent)
            print('my depth' + str(my_distance))
            print('santa depth' + str(index))
            print(santa_parent)
            break
        else:
            index += 1
            print(str(santa_parent) + "," + str(index))