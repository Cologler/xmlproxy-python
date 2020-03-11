# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import pytest

from xmlproxy import et, text_list_property, tostring

def test_text_list_property():
    class Root(et.Element):
        tags = text_list_property('tag')

    r = Root('root')
    assert tostring(r) == '<root></root>'

def test_text_list_property_set():
    class Root(et.Element):
        tags = text_list_property('tag')

    r = Root('root')
    r.tags = ['set1', 'set2']
    assert tostring(r) == '<root><tag>set1</tag><tag>set2</tag></root>'
    r.tags = ['set3', 'set4']
    assert tostring(r) == '<root><tag>set3</tag><tag>set4</tag></root>'

def test_text_list_property_del():
    class Root(et.Element):
        tags = text_list_property('tag')

    r = Root('root')
    r.tags = ['del1', 'del2']
    del r.tags
    assert tostring(r) == '<root></root>'

def test_text_list_property_append():
    class Root(et.Element):
        tags = text_list_property('tag')

    r = Root('root')
    assert len(r.tags) == 0
    r.tags.append('a')
    r.tags.append('b')
    assert tostring(r) == '<root><tag>a</tag><tag>b</tag></root>'

def test_text_list_property_extend():
    class Root(et.Element):
        tags = text_list_property('tag')

    r = Root('root')
    assert len(r.tags) == 0
    r.tags.extend(['c', 'd'])
    assert tostring(r) == '<root><tag>c</tag><tag>d</tag></root>'
