#!usr/bin/env python
# 
from nose.tools import *
from calculator import match,scan,calculator

def setUp():
    print 'function match set up'
def test_plus():
    result = match(scan('1+1'))
    assert result == 2

def test_minus():
    result = match(scan('1-100'))
    assert result == -99

def test_mult():
    result = match(scan('2*100'))
    assert result == 200
def test_div():
    result = match(scan('100/50'))
    assert result == 2

def test_mod():
    result = match(scan('100%3'))
    assert result == 1

def test_single_mix():
    result = match(scan('1+1000*10+200/2-100%4'))
    assert result == 10101
''' test_double_mix测试失败，有空在想解决办法'''
def test_double_mix():
    result = match(scan('1+1000*10*1*1+200/2+200/2+1+1-100%4-100%4'))
    assert result == 10203

def test_calculator():
    calculator('1+1')

def tearDown():
    print 'function match tear down'