#map, filter, reduce

"""
map filter reduce 三个函数能为 函数式编程 提供便利。
"""

"""
map 会将一个函数映射到一个输入列表的所有元素上。
map(function_to_apply, list_of_inputs)
把列表中所有元素一个个地传递给一个函数，并收集输出。
"""


#map
def chapter4():
    pass

    def normal():
        items = [1, 2, 3, 4, 5]
        squared = []

        for i in items:
            squared.append(i ** 2)

        print(squared)
    
    #简单 而 漂亮的方式
    """
    大多数的时候，我们使用匿名函数（lamdba）来配合使用 map

    """
    def map_test():
        items = [1, 2, 3, 4, 5]
        squared = list(map(lambda x : x **2, items))

        print(squared)

    def map_funcs():
        """
        map不仅用于 一列表的输入， 还可以用于 一列表的函数！
        """
        def multiply(x):
            return (x * x)
        def add(x):
            return (x + x)
        
        funcs = [multiply, add]

        for i in range(5):
            value = map(lambda x : x(i), funcs)
            print(list(value))

    normal()
    map_test()

    print("map list is list of functions !!!")
    map_funcs()


if __name__ == "__main__":
    chapter4()