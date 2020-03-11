# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import pytest

from xmlproxy import (
    et,
    text_property, text_list_property, element_property, element_list_property,
    tostring
)

def test_element_property():
    class Root(et.Element):
        abc = element_property('abc')

    r = Root('root')
    assert r.abc is None
    r.abc = et.Element('abc')
    r.abc.text = '12'
    r.abc.set('x', '33')
    assert tostring(r) == '<root><abc x="33">12</abc></root>'

def test_text_property():
    class Root(et.Element):
        abc = text_property('abc')

    r = Root('root')
    assert r.abc is None
    r.abc = '12'
    assert tostring(r) == '<root><abc>12</abc></root>'

def test_element_list_property():
    class Root(et.Element):
        abc = element_list_property('abc')

    r = Root('root')
    assert r.abc is not None
    assert len(r.abc) == 0
    r.abc.append(et.Element('abc'))
    r.abc.new_sub().text = 'ddd'
    assert tostring(r) == '<root><abc></abc><abc>ddd</abc></root>'

def test_element_list_property_with_type():
    class Name(et.Element):
        pass

    class Root(et.Element):
        abc: Name = element_list_property('abc', eltype=Name)

    r = Root('root')
    assert r.abc is not None
    assert len(r.abc) == 0
    with pytest.raises(TypeError):
        r.abc.append(et.Element('abc'))
    subel = r.abc.new_sub()
    assert isinstance(subel, Name)
    subel.text = 'ddd'
    assert tostring(r) == '<root><abc>ddd</abc></root>'
