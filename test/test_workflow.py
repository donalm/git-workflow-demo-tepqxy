#!/usr/bin/env python
"""Tests for workflow."""

from workflow import counter


def test_increment():
    c = counter.Counter(1)
    value = c.increment()
    assert value == 2

def test_decrement():
    c = counter.Counter(1)
    value = c.decrement()
    assert value == 0
