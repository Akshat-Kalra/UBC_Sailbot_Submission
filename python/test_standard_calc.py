from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():    #tests for 0
    assert bound_to_180(0) == 0

def test_bound_basic2():    #tests for negative angles
    assert bound_to_180(-200) == 160

def test_bound_basic3():    #tests for positive angles
    assert bound_to_180(300) == -60

def test_bound_multiples():    #tests for multiples of 360
    assert bound_to_180(720) == 0

def test_bound_boundary1():    #test the boundary cases
    assert bound_to_180(180) == -180

def test_bound_boundary2():    #test the boundary cases
    assert bound_to_180(-180) == -180


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)
