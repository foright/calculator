#!usr/bin/env python
# 
from nose.tools import *
from calculator import scan

def setUp():
    print 'function match set up'
def test_plus():
    result = scan('1+1')
    assert result['t'] == [] and result['str'] == '1+1' and result['f'] == ['1+1']

def test_minus():
    result = scan('1-100')
    assert result['t'] == [] and result['str'] == '1-100' and result['f'] == ['1-100']

def test_mult():
    result = scan('2*100')
    print result
    assert result['f'] == [] and result['str'] == '2*100' and result['t'] == ['2*100']

def test_div():
    result = scan('100/50')
    assert result['f'] == [] and result['str'] == '100/50' and result['t'] == ['100/50']

def test_mod():
    result = scan('100%3')
    assert result['f'] == [] and result['str'] == '100%3' and result['t'] == ['100%3']

def test_single_mix():
    result = scan('1+1000*10+200/2-100%4')
    assert result['t'] == ['1000*10', '200/2', '100%4'] and result['str'] == '1+1000*10+200/2-100%4' and result['f'] == ['1+t', 't-t', 'f+f']

def test_double_mix():
    result = scan('1+1000*10*1*1+200/2+200/2+1+1-100%4-100%4')
    print result
    assert result['t'] == ['1000*10', '1*1', '200/2', '200/2', '100%4', '100%4', 't*t'] and result['str'] == '1+1000*10*1*1+200/2+200/2+1+1-100%4-100%4' and result['f'] == ['1+t', 't+t', '1+1', 't-t', 'f+f', 'f-f', 'f+f']
def tearDown():
    print 'function match tear down'