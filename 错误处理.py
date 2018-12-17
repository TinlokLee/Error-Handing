'''
    错误处理机制：
    try...except...finally...
    except 捕获该类型错误子类
    可跨越多层调用

    抛出错误 raise

'''

# O不能做除数
try:
    print('try..')
    r = 1 / 0
    print('reslut:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')


import logging

def foo(s):
    ''' 调用栈 '''
    return 1 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        #print('Error:', e)
        logging.exception(e)
    # finally:
    #     print('Finally...')
main()
print("end")


# raise
class FuncError(ValueError):
    pass

def func(s):
    n = int(s)
    if n == 0:
        raise FuncError('invalid value: %s' % s)
    return 10 / 0

func('0')


#  顶层调用者处理异常，工作中常见
def func(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 1 / 0

def bar():
    try:
        func('0')
    except ValueError as e:
        print('ValueError')
        raise
bar()

# 定位错误源头，并修复
from functools import reduce

def foo(s):
    return int(s)

def cal(exp):
    ss = exp.split('+')
    ns = map(foo, ss)
    return reduce(lambda acc, x: acc+x, ns)

def main():
    r = cal('100 + 200 + 123')
    print('100 + 200 + 123 =', r)
    r = cal('99 + 88 + 1.1')
    print('99 + 88 + 1.1 =', r)

main()