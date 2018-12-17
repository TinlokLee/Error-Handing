'''
    文档测试doctest模块
    使用: doctest.testmod()
    作用：
    不但可以用来测试，还可以直接作为示例代码，通过某些文档生成工具
    自动把包含doctest注释提取出来
'''
def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    ?
    >>> fact(-1)
    ?
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()