#   Shajra Application 
import tkinter as tk

WINDOW_SIZE = '1000x800'
VERTICAL_SIZE = '400x800'
HORIZONTAL_SIZE = '1000x400'

class Node:
    def __init__(self, name, parent):
        self.__name = name 
        self.__parent = parent
        self.__child = []

    def update_child(self, child_node):
        self.__child.append(child_node)

    def get_name(self):
        return self.__name
    
    def get_parent(self):
        return self.__parent
    
    def get_child(self):
        return self.__child


class tree:
    window = None
    canvas_row = 0
    space_length = 0
    desired_node = None

    def set_desired_node(self):
        self.desired_node = None
    
    def createLabel(self, root, row, col, text_value):
        label = tk.Label(root, text=text_value)
        label.grid(row=row, column=col)
    
    def retrieve_input(self, textBox, parent_name):
        inputValue=textBox.get("1.0","end-1c")
        self.add_by_name(inputValue, parent_name)
        save_family_tree_data_in_text_file()

    def add_from_gui(self, parent_name):
        root = tk.Tk()
        root.geometry(HORIZONTAL_SIZE)
        textBox=tk.Text(root, height=1, width=30)
        textBox.pack()
        buttonCommit=tk.Button(root, height=1, width=15, text="Add New Member", command=lambda: self.retrieve_input(textBox, parent_name))
        buttonCommit.pack()

    def createFrame(self, root, row, col, text_value):
        button = tk.Button(root, text='\u2191', command=lambda : self.display_vertical(text_value)).pack(side=tk.LEFT)
        label = tk.Button(root, text=text_value, command=lambda: self.add_from_gui(text_value)).pack(side=tk.LEFT)
        button = tk.Button(root, text='\u2192', command=lambda : self.display_horizontal(text_value)).pack(side=tk.LEFT)
        root.grid(row=row, column=col, padx=0)

    def add_by_name(self, name, parent_name):
        self.set_desired_node()
        self.search_desired_node(parent_name, ALPHA_NODE)
        self.add_new_node(name, self.desired_node)

    def add_new_node(self, name, parent):
        node = None
        if parent is None:
            print('Parent is None aganist -> ', name)
        else:
            node = Node(name, parent)
            parent.update_child(node)
        return node
    
    def display_vertical(self, name):
        self.window = tk.Tk()
        self.window.geometry(VERTICAL_SIZE)
        
        self.set_desired_node()
        self.search_desired_node(name, ALPHA_NODE)
        self.vertical_display(self.desired_node)
        
        self.window.mainloop()
        
    def vertical_display(self, node): 
        if node is None:    
            return
        self.vertical_display(node.get_parent())
        # GUI Component
        self.createLabel(self.window, self.canvas_row, 1, node.get_name())
        self.createLabel(self.window, self.canvas_row + 1, 1, '  |  ')
        self.canvas_row += 2

        print(node.get_name())
        print('  |  ')

    def display_horizontal(self, name):
        self.window = tk.Tk()
        self.window.geometry(HORIZONTAL_SIZE)

        self.set_desired_node()
        self.search_desired_node(name, ALPHA_NODE)
        self.horizontal_display(self.desired_node)

        self.window.mainloop()

    def horizontal_display(self, node):
        if node.get_parent() is None:
            print('\nSorry No Data Found\n')
            return
        else:
            node = node.get_parent()
            count = 0
            for child in node.get_child():
                self.createLabel(self.window, self.canvas_row, count, child.get_name())
                self.createLabel(self.window, self.canvas_row , count + 1, '  |  ')
                count += 3
                print(child.get_name(), ' | ', end="")

    def complete_traversal(self, name):
        self.window = tk.Tk()
        self.window.geometry(WINDOW_SIZE)
        
        self.set_desired_node()
        self.search_desired_node(name, ALPHA_NODE)
        self.traverse(self.desired_node)
        
        self.window.mainloop()

    def traverse(self, node):
        gridframe = tk.Frame(self.window)   
        if node is None:
            return
        else:
            if len(node.get_child()) == 0:
                # GUI Component
                self.format_gui_tree()
                self.createFrame(gridframe, self.canvas_row, self.space_length, node.get_name())
                self.canvas_row += 1

                self.format_tree()
                print(node.get_name())
            else:
                 # GUI Component
                self.format_gui_tree()
                self.createFrame(gridframe, self.canvas_row, self.space_length, node.get_name())                
                self.canvas_row += 1

                self.format_tree()
                print(node.get_name())

                self.space_length += 1
                for child in node.get_child():
                    self.traverse(child)
                self.space_length -= 1

    def search_desired_node(self, name, node):
        if node is None:
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

    def format_gui_tree(self):
        string = '|'
        for i in range(self.space_length):
            self.createLabel(self.window, self.canvas_row, i, string)  


def save_family_tree_data_in_text_file():
    with open('shajra.txt', 'w+') as f:
        pass
    save_data(ALPHA_NODE)
   
def save_data(node):
    if node is None:
        return
    else:
        with open('shajra.txt', 'a') as f:
            if node.get_parent() is not None:
                f.write(node.get_name() + ',' + node.get_parent().get_name() + '\n')
            else:    
                f.write(node.get_name() + ',' + 'None' + '\n')
        if len(node.get_child()) == 0:
           pass
        else:
            for child in node.get_child():
                save_data(child)

def intialize_tree(T):
    try:
        with open('shajra.txt', 'r') as f:
            f.readline()
            lines = f.read().split('\n')
            for line in lines:
                if line:
                    names = line.split(',')
                    T.add_by_name(names[0], names[1])
    except Exception:
        with open('shajra.txt', 'w+') as f:
            pass

def options():
    print('\n')
    print('[1] Add New Member   [name,parent]')
    print('[2] Display Vertical [name]')
    print('[3] Display Siblings [name]')
    print('[4] Display Tree     [name]')
    print('[5] Save Family Tree \n')

def handle_user_input(T):
    T.complete_traversal('Deen')
    options()
    # user_input = int(input('Enter Option Number: '))
    while True:
        T.complete_traversal('Deen')
        # if user_input == 1:
        #     name = input('\nEnter Member Name: ')
        #     parent = input('\nEnter Parent Name: ')
        #     T.add_by_name(name, parent)
        # elif user_input == 2:
        #     name = input('\nEnter Member Name: ')
        #     T.display_vertical(name)
        # elif user_input == 3:
        #     name = input('\nEnter Member Name: ')
        #     T.display_horizontal(name)
        # elif user_input == 4:
        #     name = input('\nEnter Member Name: ')
        #     T.complete_traversal(name)
        # elif user_input == 5:
        #     save_family_tree_data_in_text_file()
        #     print('\nSaved in TEXT File\n')
        # else:
        #     options()
        # user_input = int(input('\nEnter Option Number: '))
        

ALPHA_NODE = Node('Deen', None)

if __name__ == "__main__":
    print("\nShajra Console Application\n")
    print("__________________________\n")

    T = tree()
    intialize_tree(T)
    handle_user_input(T)
    print('\n')

