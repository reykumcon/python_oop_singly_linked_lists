# Adding a Value to the Front

class SLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    def print_value(self):
        runner = self.head
        while (runner != None):
            print(runner.val)
            runner = runner.next
        return self
    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self
    def remove_from_front(self):
        if self.head.next == None:
            self.head = None
        else:
            self.head = self.head.next
        return self

    def remove_from_back(self):
        if self.head.next == None:
            self.head = None
        else:
            runner = self.head
            while(runner.next != None):
                prev_runner = runner
                runner = runner.next
            prev_runner.next = None
        return self

    # def remove_val(self, val):
    #     runner = self.head
        

my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_value()
my_list.remove_from_back()
my_list.print_value()
my_list.remove_from_front()
my_list.print_value()