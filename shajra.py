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

ALPHA_NODE = Node('Deen', None)

class tree:
    space_length = 0
    desired_node = None
    
    def set_desired_node(self):
        self.desired_node = None
    
    def add_by_name(self, name, parent_name):
        self.set_desired_node()
        self.search_desired_node(parent_name, ALPHA_NODE)
        self.add_new_node(name, self.desired_node)

    def add_new_node(self, name, parent):
        node = None
        print('\n PARENT === ', parent.get_name())
        if parent is None:
            print('Parent is None aganist -> ', name)
        else:
            node = Node(name, parent)
            parent.update_child(node)
        return node
    
    def display_vertical(self, name):
        self.set_desired_node()
        self.search_desired_node(name, ALPHA_NODE)
        self.vertical_display(self.desired_node)
        
    def vertical_display(self, node):    
        if node is None:
            return
        self.vertical_display(node.get_parent())
        print(node.get_name())
        print('  |  ')

    def display_horizontal(self, name):
        self.set_desired_node()
        self.search_desired_node(name, ALPHA_NODE)
        self.horizontal_display(self.desired_node)

    def horizontal_display(self, node):
        if node.get_parent() is None:
            print('\nSorry No Data Found\n')
            return
        else:
            node = node.get_parent()
            for child in node.get_child():
                print (child.get_name(), ' | ', end="")

    def complete_traversal(self, name):
        self.set_desired_node()
        self.search_desired_node(name, ALPHA_NODE)
        self.traverse(self.desired_node)

    def traverse(self, node):
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
                    self.traverse(child)
                self.space_length -= 1


    def search_desired_node(self, name, node):
        if node is None:
            print('\nsearch node in none \n')
            return
        elif node.get_name() == name:
            self.desired_node = node
        else:
            if len(node.get_child()) != 0:
                self.space_length += 1
                for child in node.get_child():
                    self.search_desired_node(name, child)
                self.space_length -= 1

    def format_tree(self):
        for i in range(self.space_length):  
            print('  |', end="")


def save_family_tree_data_in_text_file():
    save_data(ALPHA_NODE)
   
def save_data(node):
    if node is None:
        return
    else:
        with open('shajra.txt', 'a+') as f:
            if node.get_parent() is not None:
                f.write(node.get_name() + ',' + node.get_parent().get_name() + '\n')
            else:    
                f.write(node.get_name() + ',' + 'None' + '\n')
        if len(node.get_child()) == 0:
           pass
        else:
            for child in node.get_child():
                save_data(child)


if __name__ == "__main__":
    print('\tShajra Python Application\n')
    f1 = ALPHA_NODE
    T = tree()

    with open('shajra.txt', 'r') as f:
        f.readline()
        lines = f.readlines()
        for line in lines:
            names = line.split(',')
            T.add_by_name(names[0], names[1])
            print(names[0], ' -- ',  names[1])


    # f2 = T.add_new_node('Akbar', f1) 
    # f20 = T.add_new_node('Bashir', f1) 
    
    # f3 = T.add_new_node('Ihsan', f2) 

    # f31 = T.add_new_node('Inam', f2) 
    # f310 = T.add_new_node('Shahzeb', f31) 
    # f311 = T.add_new_node('Danial', f31) 
    # f312 = T.add_new_node('Ali', f31) 

    # f32 = T.add_new_node('Anwar', f2) 
    # f320 = T.add_new_node('Jazib', f32) 
    
    # f40 = T.add_new_node('Rizwan', f3)
    # f41 = T.add_new_node('Adnan', f3) 
    # f42 = T.add_new_node('Anzil', f3) 

    name = 'Adnan'

    # T.display_vertical(name)
    # T.display_horizontal(name)

    # T.complete_traversal(name)

    # save_family_tree_data_in_text_file()
    print('\n')

