#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = (a and not b) or (b and not a)
        carry.next = a and b
        
    return instances()


# @block
# def fullAdder(a, b, c, soma, carry):
#     soma1 = Signal(bool(0))
#     @always_comb
#     def comb():

#         carry.next = (a and b) or (a and c) or (b and c)
#         soma.next = (not a and not b and c) or (not a and b and not c) or (a and b and c) or (a and not b and not c)

#     return instances()


# @block
# def fullAdder(a, b, c, soma, carry):
#     soma1 = Signal(bool(0))
#     carry1 = Signal(bool(0))
#     soma2 = Signal(bool(0))
#     carry2 = Signal(bool(0))

#     half1 = halfAdder(a,b,soma1,carry1)
#     half2 = halfAdder(c,soma1,soma2,carry2)


#     @always_comb
#     def comb():
#         soma.next = soma2
#         carry.next = carry2 | carry1

#     return instances()


@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]
    haList = [None for i in range(2)]  

    haList[0] = halfAdder(a, b, s[0], s[1]) 
    haList[1] = halfAdder(c, s[0], soma, s[2])

    @always_comb
    def comb():
        carry.next = s[1] | s[2]

    return instances()



@block
def adder2bits(x, y, soma, carry):
    carry2 = Signal(bool(0))

    half = halfAdder(x[0],y[0],soma[0],carry2)
    full = fullAdder(x[1],y[1],carry2,soma[1],carry)

    return instances()


@block
def adder(x, y, soma, carry):
    n = len(x)
    faList = [None for i in range(n)]
    carryList = [Signal(bool(0)) for i in range(n)]
    somaList = [Signal(bool(0)) for i in range(n)]

    # faList[0] = fullAdder(x[0],y[0],0,soma[0],carryList[0])

    for i in range(n):
        faList[i] = fullAdder(x[i],y[i],(0 if i==0 else carryList[i-1]),somaList[i],carryList[i])


    @always_comb
    def comb():
        carry.next = carryList[n-1]
        for i in range(n):
            soma[i].next = somaList[i]
        
 
    return instances()
