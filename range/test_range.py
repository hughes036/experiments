
from range.range import Range

def test_add():
    r = Range()
    r.add(0, 100)
    assert r.query(50) == True
    assert r.query(0) == True
    assert r.query(100) == True
    assert r.query(-1) == False
    assert r.query(101) == False

def test_remove_middle():
    r = Range()
    r.add(0, 100)
    r.remove(25, 75)
    # middle of removed range
    assert r.query(50) == False
    # edges of removed range
    # left
    assert r.query(25) == False
    assert r.query(24) == True
    # right
    assert r.query(75) == False
    assert r.query(76) == True

def test_remove_right_edge():
    r = Range()
    r.add(0, 100)
    r.remove(80, 200)
    assert r.query(80) == False
    assert r.query(79) == True

def test_remove_left_edge():
    r = Range()
    r.add(0, 100)
    r.remove(-10, 50)
    assert r.query(50) == False
    assert r.query(51) == True

def test_remove_both_edges():
    r = Range()
    r.add(0, 100)
    r.remove(-10, 200)
    assert r.query(1) == False
    assert r.query(100) == False

def test_remove_beyond_right_edge():
    r = Range()
    r.add(0, 100)
    r.remove(-10, -200)
    assert r.query(0) == True
    assert r.query(100) == True


def test_remove_beyond_left_edge():
    r = Range()
    r.add(0, 100)
    r.remove(200, 300)
    assert r.query(0) == True
    assert r.query(100) == True