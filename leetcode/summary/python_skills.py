#-*- coding:utf-8 -*-

#1.python list1.sort()为in_place  sorted(list1)会创建一个新的list
#2.range()会产生一个缓存的list 而xrange()更像是生成器
#3.python矩阵处理 row = len(matrix)   col = len(matrix[0]) if row else 0   python中None False  [] "" {} ()都是False
#4.python列表生成 lst = [0 for i in xrange(0,5)]  二维数组 lst = [ [for i in xrange(0,4)] for j in range(0,2)]
#5.字典赋值给不存在的键 dic.get(key,0)
#6.字典赋值 dict["key"].append()
#7.Python中字符串不能反转，但列表可以反转 str1 = "abcd"  str1[::-1]  "".join([string].reverse())
#8.Python中自带的计数器  Counter 返回一个字典
#9.判断奇数偶数   if num%2==0  如果是True则为偶数 或者 if(num&1) == 0