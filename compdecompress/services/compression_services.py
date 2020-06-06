
class Node():
    def __init__(self, char):
        self.char = char
        self.count = 1
    
    def add_count(self):
        self.count += 1

class Stack():
    def __init__(self):
        self.arr = []
        self.top = -1
    
    def peek_value(self):
        if self.top == -1:
            return
        return self.arr[self.top].char

    def push(self, char):
        if self.top == -1:
            self.arr.append( Node(char))
            self.top += 1
        elif self.peek_value() == char:
            self.arr[self.top].add_count()
        else:
            self.arr.append( Node(char))
            self.top += 1

class CompressDecompress():

    def __init__(self, str, mode):
        self.mode = mode
        if mode == 'compress':
            self.decompressed_str = str
            self.compressed_str = self.compress(str)
        else:
            self.decompressed_str = self.decompress(str)
            self.compressed_str = str

    def compress(self, string):
        stk = Stack()
        for char in string:
            stk.push(char)
        compressed_str = ""
        for node in stk.arr:
            compressed_str += str(node.count) + str(node.char)

        if compressed_str >= string:
            return None
        return compressed_str

    def get_compressed_str(self):
        return self.compressed_str

    def decompress(self, str):
        pass

    def get_decompressed_str(self):
        return self.decompressed_str


if __name__ == "__main__":
    obj1 = CompressDecompress("aaaabbcccccdde", "compress")
    print(obj1.get_compressed_str())
