#!/usr/bin/env python
# -*- coding: utf-8 -*-


# @Site    : 变量类型
# @File    : Variable.py
# @Author  : daimin
# @Time    : 2019/4/24 22:40
# @Desc     :

'''
弱类型：
1. 无序声明即可使用；
2. 类型可变；
'''
import keyword

# 弱类型 type判断类型
name = 'daimin'
print(type(name))

name = 5
print(type(name))

# print输出多个变量 sep 分隔
girlName = 'Rose'
age = 20
print("女孩的名字：",girlName, "年龄：", age, sep='*')

# print默认换行 end='\n'  重设end可改变换行或者间隔
print(1, end='= ')
print(2, end='=')

# 输出到文件
f = open('write', 'w')
print('苟有恒，何必三更起五更眠；', file=f)
print('最无益，只怕一日曝十寒。', file=f)
f.close()

# 所有关键字
print('\n')
print(keyword.kwlist)