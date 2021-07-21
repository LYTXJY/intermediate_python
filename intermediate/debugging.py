"""
python 进阶

"""
import time

# debugging

def debugging_test():
    """更多的操作，请看官方文档
    """
    pass



def timmer(func):
    def deco(*args, **kwargs):
        print('\n函数：{_funcname_}开始运行：'.format(_funcname_=func.__name__))
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print('函数:{_funcname_}运行了 {_time_}秒'
              .format(_funcname_=func.__name__, _time_=(end_time - start_time)))
        return res
    return deco

#chapter3

def chapter3():
  
    """
    生成器：generators

    首先我们要理解迭代器（iteratiors）
    迭代器是一个让程序员可以遍历一个容器（特别是列表）的对象

        可迭代对象：iterable
        迭代器：iterator
        迭代：iteration

    上述弄明白后，再看生成器（generators）

    可迭代对象：iterable
    python 中 如果定义了 __iter__（返回一个迭代器） 或者 __getitem__（可以支持下标索引） 方法，
    那么他就是一个迭代器。
    可迭代对象就是能够提供迭代器的任意对象。

    迭代器：iterator
    任意对象，定义__next__方法，它就是一个迭代器。

    迭代：iteration
    从列表中取出一个元素的过程，称为迭代。
    使用一个循环来遍历某个东西时，这个过程本身就是迭代。

    生成器也是一种迭代器，但是你只能对其迭代一次！
    这是因为它们并没有把所有的值存在内存中，而是在运行时生成值。
    你通过遍历来使用他们，要么用一个for循环，要么将它们传递给任意可以进行迭代的函数和结构。
    大多数时候 生成器 是以 函数来实现的。然而，它们并不返回一个值，而是yield（暂且翻译为 “生出”）一个值。
    以下是生成器的简单例子：

    """

    # def generator_function():
    #     for i in range(10):
    #         yield i
    # for item in generator_function():
    #     print(item)

    """
    这个案例不实用。生成器最佳应用场景是：
    你不想同一时间将所有计算出来的大量结果 集体 分配到 内存中，特别是结果 里 还包含循环。
    这样会消耗大量资源。
    许多python2里的标准库函数都会返回列表，而python3都修改成了返回生成器，因为生成器占用更少的资源！
    以下是计算 斐波那契额数列 的生成器：
    """

    def fibonacci_test():

        #@timmer
        def fibon(n):
            #Fibonacci number
            a = b = 1
            for i in range(n):
                yield a
                a, b = b, a + b

        def fibon_iteration(n):
            """
            计算很大的输入参数时，用尽所有的资源。
            我们说过 生成器 使用一次迭代，但我们没有测试过。
            python 内置函数 ：next()。它允许我们获取一个序列的下一个元素。
            """
            a = b = 1
            results = []
            for i in range(n):
                results.append(a)
                a, b = b, a + b
            return results


        time_start = time.time()
        for x in fibon(100):
            print(x)
            # pass
        time_end = time.time()
        time_c = time_end - time_start
        print("time cost ", time_c, "s")

        print("*"*100)

        time_start = time.time()
        for x in fibon_iteration(100):
            print(x)
        time_end = time.time()
        time_c = time_end - time_start
        print("time cost ", time_c, "s")

    # fibonacci_test()

    def yield_test():
        def generator_function():
            for i in range(3):
                yield i
        gen = generator_function()
        print(next(gen))
        print(next(gen))
        print(next(gen))
        # print(next(gen))
        """
        在yield 所有值后，next()触发了一个StopIteration的异常.
        这个异常告诉我们，所有的值已经都被yield完了。
        for循环不会出现这个异常。因为for循环会自动捕捉这个异常并停止调用next().
        """
    
    def yield_test_2():
        my_string = "Yasoob"
        # next(my_string)
        #TypeError : 'str' object is not an iterator
        #str 对象不是一个迭代器
        #str 是一个可迭代对象，但不是一个迭代器。这意味着不可以直接对其进行迭代操作。


        """
        下一个内置函数，iter。它将根据一个  可迭代对象  返回一个  迭代器对象  。
        """

        my_iter = iter(my_string)
        print(next(my_iter))
        print(next(my_iter))
        print(next(my_iter))
        print(next(my_iter))


    
    # yield_test()
    yield_test_2()

    """
    总结：
    爱上学习生成器。一定要记住，想要完全掌握这个概念，你只有使用它。
    确保你按照这个模式，并在生成器对你有意义的任何时候都使用它。你绝对不会失望的。
    """



if __name__ == "__main__":
    chapter3()