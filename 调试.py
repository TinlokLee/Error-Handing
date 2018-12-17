'''
    程序调试修复BUG
    1 print
    2 assert断言代替Print
      python -0 err.py 把所有assert语句当做pass
    3 logging
      需要配置日志信息
      import logging
      logging.basicConfig(level=logging.INFo)
    4 python调试器pdb--单步执行
      启动命名：python -m pdb err.py
      查看变量：p 变量名
      继续运行：c
      退出程序：q
    5 pdb.set_trace()设置一个断点
      import pdb


'''