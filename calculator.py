#!usr/bin/env python
#--- coding=utf-8 ----
# 1. 支持四则运算 +-×/% 
# 2. 支持数论中的全部类型
# 
# 方法论：
# 1.输入值分解，按优先级排列
# 2.分步计算
# 
# 
# import sys
import re

'''扫描输入'''
def scan(str):
    match = {'str':str, 't':[],'f':[]}
    patten = {'t':'[\d|\w]+[\*/%][\d|\w]+', 'f':'[\d|\w]+[+-][\d|\w]+','double_t':'\w+[\*/%]\w+'}
    while str != 'f' and str != 't': 
        while re.search(patten['t'], str):
            for co in re.findall(patten['t'], str):
                match['t'].append(co)
            str = re.sub(patten['t'], 't', str)
            print str
        while re.search(patten['f'], str):
            for co in re.findall(patten['f'], str):
                match['f'].append(co)
            str = re.sub(patten['f'], 'f', str)
    return match

'''匹配计算'''
def match(tokens):
    for value in tokens['t']:
        position = tokens['t'].index(value)
        if 't' in value:
            if value.count('t') > 1:
                value = str(tokens['t'][position-2])+value[1]+str(tokens['t'][position-1])
            else:
                value = value.replace('t',str(tokens['t'][position-1]))
        if '*' in value:
            param = value.split('*')
            tokens['t'][position] = int(param[0])*int(param[1])
        elif '/' in value:
            param = value.split('/')
            tokens['t'][position] = int(param[0])/int(param[1])
        elif '%' in value:
            param = value.split('%')
            tokens['t'][position] = int(param[0])%int(param[1])

    if len(tokens['f']) == 0:
        return tokens['t'][len(tokens['t'])-1]

    for value in tokens['f']:
        position = tokens['f'].index(value)
        if 't' in value:
            if value.count('t') > 1:
                value = str(tokens['t'][position])+value[1]+str(tokens['t'][position+1])
            else:
                value = value.replace('t',str(tokens['t'][position]))
        if 'f' in value:
            if value.count('f') > 1:
                value = str(tokens['f'][position-2])+value[1]+str(tokens['f'][position-1])
            else:
                value = value.replace('f',str(tokens['f'][position-1])) 
        if '+' in value:
            param = value.split('+')
            tokens['f'][position] = int(param[0])+int(param[1])
        elif '-' in value:
            param = value.split('-')
            tokens['f'][position] = int(param[0])-int(param[1])
    return tokens['f'][len(tokens['f'])-1]

'''计算输出'''
def calculator(s):
   token = scan(s)
   print  match(token)

if __name__ == "__main__":
    s = raw_input(str)
    calculator(s)