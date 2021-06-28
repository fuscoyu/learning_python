<!-- TOC -->

- [1. python 2/3的区别](#1-python-23的区别)
    - [1.1. Python3的优化化](#11-python3的优化化)
    - [1.2. Python3 新增](#12-python3-新增)
    - [1.3. Python3 改进](#13-python3-改进)
    - [1.4. Python 2/3工具](#14-python-23工具)

<!-- /TOC -->
# 1. python 2/3的区别

## 1.1. Python3的优化化

1. print 成为函数
2. 编码问题 python3 不在有unicode对象，默认str就是unicode     
3. 除法变化。python3 除号返回浮点数  整除使用 "//"
4. 类型注解（type hint)。 帮助ide实现类型检查  通过第三方工具mypy 进行类型检查

    ```bash
    def hello(name: str) -> str:
        return 'hello' + name
    ```

5. 优化super() 方便直接调用父类函数
6. 高级的解包操作。 a, b, *rest = range(10)
7. 限定关键字参数
8. python3 重新抛出异常不会丢失栈信息  raise  xxxError from xxxError
9.  一切返回迭代器 range, zip, map, dict, values, etc. all iterators

## 1.2. Python3 新增

1. yield from 链接子生成器
2. asyncio 内置库， async/await 原生协程支持异步编程
3. 新的内置库 enum（枚举）, mock（单元测试 ）, asynico, ipaddress, concurrent.futures 等

## 1.3. Python3 改进

生成的pyc文件统一放到__pycache__

一些内置库的修改  urllib,selector等

性能的优化等

## 1.4. Python 2/3工具

six模块

2to3 等工具转换代码

\_\_future\_\_

