#   Shajra Application 
 
class Node:
    def __init__(self, name, parent):
        self.__name = name 
        self.__parent = parent
        self.__child = []

    def update_child(self, child_node):
        # print('\nChild Name = ', child_node.get_name())
        # print('Parent Name = ', child_node.get_parent().get_name())
        # print('# of Childs = ', len(self.__child))
        self.__child.append(child_node)

    def get_name(self):
        return self.__name
    
    def get_parent(self):
        return self.__parent
    
    def get_child(self):
        return self.__child

class tree:
    space_length = 0
    
    def add_new_node(self, name, parent):
        node = None
        if parent is None:
            print('Parent is None aganist -> ', name)
        else:
            node = Node(name, parent)
            parent.update_child(node)
        return node
    
    def display_vertical(self, node):
        if node is None:
            return
        self.display_vertical(node.parent)
        print(node.name)
        print('  |  ')

    def display_horizontal(self, node):
        if node.get_parent() is None:
            print('\nSorry No Data Found\n')
            return
        else:
            node = node.get_parent()
            for child in node.get_child():
                print (child.get_name(), ' | ', end="")

    def complete_traversal(self, node):
        # print(node.get_name())
        if node is None:
            return
        else:
            if len(node.get_child()) == 0:
                self.format_tree()
                print(node.get_name())
            else:
                self.format_tree()
                print(node.get_name())
                self.space_length += 1
                for child in node.get_child():
                    # self.format_tree()
                    self.complete_traversal(child)
                self.space_length -= 1

    def format_tree(self):
        for i in range(self.space_length):  
            print('  |', end="")


if __name__ == "__main__":
    print('\tShajra Python Application\n')
    f1 = Node('Deen ', None)

    T = tree()
    f2 = T.add_new_node('Akbar', f1) 
    f20 = T.add_new_node('Bashir', f1) 
    
    f3 = T.add_new_node('Ihsan', f2) 

    f31 = T.add_new_node('Inam', f2) 
    f310 = T.add_new_node('Shahzeb', f31) 
    f311 = T.add_new_node('Danial', f31) 
    f312 = T.add_new_node('Ali', f31) 

    f32 = T.add_new_node('Anwar', f2) 
    f320 = T.add_new_node('Jazib', f32) 
    
    f40 = T.add_new_node('Rizwan', f3)
    f41 = T.add_new_node('Adnan', f3) 
    f42 = T.add_new_node('Anzil', f3) 

    # T.display_vertical(f40)
    # T.display_horizontal(f40)
    T.complete_traversal(f1)
    print('\n\n')

