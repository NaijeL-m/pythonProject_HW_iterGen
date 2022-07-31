
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class list_range:
    def __init__(self,l):
        self.start = l[0][0]
        self.end = l[-1][-1]
        self.l = l
        self.x = 0
        self.y = -1
    def __iter__(self):
        self.cursor = self.start
        return self
    def __next__(self):
        if self.cursor == self.l[self.x][-1]:
            self.x += 1
            self.y = -1
        if self.cursor == self.end:
            raise StopIteration
        self.y += 1
        self.cursor = self.l[self.x][self.y]
        return self.cursor

def my_range(l):
    x = 0
    y = 0
    start_range = l[0][0]
    while start_range != l[-1][-1]: #ибо альтернативное условие ((x != (len(l)-1)) and (y != (len(l[-1])-1)))
        yield start_range
        y += 1
        if y == len(l[x]):
            x += 1
            y = 0
        start_range = l[x][y]
    yield start_range

for i in list_range([["qw","e","asd",False],["zx","c","rty",None]]):
    print(i)
print([i for i in list_range([["qw","e","asd",False],["zx","c","rty",None]])])
for i in my_range([["qw","e","asd",False],["zx","c","rty",None]]):
    print(i)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
