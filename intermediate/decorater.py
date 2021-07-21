from functools import wraps


def test1():
    def logit(func):
        """logging
        """
        wraps(func)
        def with_logging(*args, **kwargs):
            print(func.__name__ + "was called")
            return func(*args, **kwargs)
        return with_logging

    @logit
    def addition_func(x):
        """do some math!
        """
        return x + x

    result = addition_func(4)
    print(result)

def test2():

    def logit(logfile = 'out.log'):
        def logging_decorator(func):
            @wraps(func)
            def wrapped_function(*args, **kwargs):
                log_string = func.__name__ + "_was_called!"
                print(log_string)
                with open(logfile, 'a') as opened_file:
                    opened_file.write(log_string + '\n')
                return func(*args, **kwargs)
            return wrapped_function
        return logging_decorator
    

    
    """
    注意，这是带参数的装饰器。
    即： @logit()
    之前的装饰器 是不带（）的，是没有参数的
    """
    @logit()
    def myfunc1():
        pass

    myfunc1()

    @logit(logfile = "out2.log")
    def myfunc2():
        pass

    myfunc2()


def test3():
    """装饰器类
    类也可以用来构建装饰器。以一个类而不是一个函数的方式，来重新构建logit。
    """

    class logit(object):
        def __init__(self, logfile = 'out.log'):
            self.logfile = logfile

        def __call__(self, func):
            @wraps(func)
            def wrapped_function(*args, **kwargs):
                log_string = func.__name__ + "_was called!"
                print(log_string)
                with open(self.logfile, 'a') as opened_file:
                    opened_file.write(log_string + '\n')
                    self.notify()
                return func(*args ,**kwargs)
            return wrapped_function

        def notify(self):
            #logit 只打日志， 不做别的
            pass
        




if __name__ == "__main__":
    # test1()
    test2()

