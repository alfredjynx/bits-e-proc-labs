#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import math
from myhdl import *
from ula.ula_modules import adder


@block
def dff(q, d, clk, rst):
    @always_seq(clk.posedge, reset=rst)
    def seq():
        q.next = d

    return instances()


@block
def contador(leds, clk, rst):
    
    @always_seq(clk.posedge, reset=rst)
    def seq():
        valor = leds + 1
        leds.next = valor

    return instances()


@block
def blinkLed(led, time, clk, rst):
    cnt = Signal(intbv(0)[32:])
    l = Signal(bool(0))

    @always_seq(clk.posedge, reset=rst)
    def seq():
        if cnt < time*5000:
            cnt.next = cnt + 1
        else:
            cnt.next = 0
            l.next = not l

    @always_comb
    def comb():
        led.next = l

    return instances()


@block
def barLed(leds, clk, rst):
    cnt = Signal(intbv(0)[32:])
    # ledr_s = [Signal(bool(0)) for i in range(len(leds))]
    i = Signal(intbv(0)[32:])
    l = Signal(bool(0))
    # c = Signal(intbv(0)[32:])

    @always_seq(clk.posedge, reset=rst)
    def seq():
        if i == 8:
            i.next = 0
            l.next = not l

        if cnt < 5000000*50000:
            cnt.next = cnt + 1
        else:
            cnt.next = 0
            i.next = i + 1
        


    @always_comb
    def comb():
        leds[i].next = l
        leds[i-1].next = not l
        
    return instances()


@block
def barLed2(leds, clk, rst):
    @always_seq(clk.posedge, reset=rst)
    def seq():
        pass

    return instances()
