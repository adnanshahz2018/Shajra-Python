#   Shajra Application 
import tkinter as tk
import tkinter as ttk

WINDOW_SIZE = '1000x700'
VERTICAL_SIZE = '400x800'
HORIZONTAL_SIZE = '800x400'
FILENAME = 'shajra.txt'

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


class ProductItem(tk.Frame):
    def __init__(self, master, message, **kwds):
        tk.Frame.__init__(self, master, **kwds)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

class ScrollableContainer(tk.Frame):
    def __init__(self, master, T, desired_node, option, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)  # holds canvas & scrollbars
        self.grid_rowconfigure(0, minsize=600, weight=1)
        self.grid_columnconfigure(0, minsize=600, weight=1)
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0)
        
        self.hScroll = tk.Scrollbar(self, orient='horizontal', command=self.canvas.xview)
        self.hScroll.grid(row=1, column=0, sticky='we')
        self.vScroll = tk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.vScroll.grid(row=0, column=1, sticky='ns')
        self.canvas.grid(row=0, column=0, sticky='nws')
        self.canvas.configure(xscrollcommand=self.hScroll.set, yscrollcommand=self.vScroll.set)
        self.frame = tk.Frame(self.canvas, width=600, height=600, bd=2)
        self.frame.grid_columnconfigure(0, weight=1)
        self.canvas.create_window(0, 0, window=self.frame, anchor='nw', tags='inner')

        T.set_window(self.frame)
        if option == 'H':
            T.horizontal_display(desired_node)
        elif option == 'V':
            T.vertical_display(desired_node)
        elif option == 'T':
            T.traverse(desired_node)
        else:
            pass

        self.canvas.bind('<Configure>', self.on_configure)

    def update_layout(self):
        self.frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        self.canvas.yview('moveto', '1.0')
        self.size = self.frame.grid_size()

    def on_configure(self, event):
        w, h = event.width, event.height
        natural = self.frame.winfo_reqwidth()
        self.canvas.itemconfigure('inner', width=w if w > natural else natural)
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))


class tree:
    window = None
    canvas_row = 0
    space_length = 0
    desired_node = None

    def set_desired_node(self):
        self.desired_node = None
    
    def set_window(self, window):
        self.window = window

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
        # label = tk.Button(root, text=text_value).pack(side=tk.LEFT)
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
        root = tk.Tk()
        root.geometry('200x200')

        self.set_desired_node()
        self.search_desired_node(name, ALPHA_NODE)

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        sc = ScrollableContainer(root, T, self.desired_node, 'V', bd=2)
        sc.grid(row=0, column=0, sticky='n')
        root.mainloop()
        
    def vertical_display(self, node): 
        if node is None:    
            return
        self.vertical_display(node.get_parent())
        # GUI Component
        root = self.window
        self.createLabel(self.window, self.canvas_row, 1, node.get_name())
        self.createLabel(self.window, self.canvas_row + 1, 1, '  |  ')
        self.canvas_row += 2

        print(node.get_name())
        print('  |  ')

    def display_horizontal(self, name):
        root = tk.Tk()
        root.geometry(HORIZONTAL_SIZE)

        self.set_desired_node()
        self.search_desired_node(name, ALPHA_NODE)

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        sc = ScrollableContainer(root, T, self.desired_node, 'H', bd=2)
        sc.grid(row=0, column=0, sticky='n')
        root.mainloop()

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
        root = tk.Tk()
        root.geometry(WINDOW_SIZE)
        
        self.set_desired_node()
        self.search_desired_node(name, ALPHA_NODE)

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        sc = ScrollableContainer(root, T, self.desired_node, 'T', bd=2)
        sc.grid(row=0, column=0, sticky='n')        
        root.mainloop()

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
    with open(FILENAME, 'w+') as f:
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
        with open(FILENAME, 'r') as f:
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


"""     TASKS & UPDATES
1. Get the Host Screen Size for the Frame and Window Size of App

"""