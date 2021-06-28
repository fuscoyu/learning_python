<!-- TOC -->

- [1. learning_python](#1-learning_python)
    - [1.1. 基础知识](#11-基础知识)
    - [1.2. [python2/3的区别](./python2_3_diff/README.md)](#12-python23的区别python2_3_diffreadmemd)

<!-- /TOC -->
# 1. learning_python
用于复习Python的仓库

## 1.1. 基础知识
1. Python 是一个动态强类型语言 （没有类型隐式转换）

```bash
>>> 1 + '1'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

2. python2/3 不兼容

3. 什么是自省？

运行时判断一个对象的类型的能力

Python一切皆对象，用type,id,instance获取对象类型信息

4. monkey patch 运行时属性替换

5. is 判断对象

6. 列表推导式

```bash
# 字典推导式
{k:v for k, v in zip(a,b)}

# list
[i for i in range(10)]

# set
(i for i in range(10)) 
返回类型为generator
```

7. 鸭子类型duck typing

[https://zh.wikipedia.org/wiki/鸭子类型](https://zh.wikipedia.org/wiki/%E9%B8%AD%E5%AD%90%E7%B1%BB%E5%9E%8B)

当看到一个鸟走起来像鸭子、游泳起来像鸭子、叫起来像鸭子、那么这只鸟就可以被称为鸭子。

在鸭子类型中，关注点在于对象的行为，能做什么。 关注的是方法、属性。不关注对象

## 1.2. [python2/3的区别](./python2_3_diff/README.md)
