from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():    # tests for 0
    assert bound_to_180(0) == 0


def test_bound_basic2():    # tests for negative angles
    assert bound_to_180(-200) == 160


def test_bound_basic3():    # tests for positive angles
    assert bound_to_180(300) == -60


def test_bound_multiples():    # tests for multiples of 360
    assert bound_to_180(720) == 0


def test_bound_boundary1():    # test the boundary cases
    assert bound_to_180(180) == -180


def test_bound_boundary2():    # test the boundary cases
    assert bound_to_180(-180) == -180


""" Tests for is_angle_between() """


def test_between_basic1():    # basic test using positive angles
    assert is_angle_between(0, 1, 2)


def test_between_basic2():    # another basic test using positive angles
    assert not is_angle_between(45, 90, 270)


def test_for_overlapping1():    # test for overlapping angles
    assert not is_angle_between(0, 0, 180)


def test_for_overlapping2():    # another test for overlapping angles
    assert not is_angle_between(0, 90, 90)


def test_for_negatives():    # test for negative angles
    assert is_angle_between(-30, -15, 0)


def test_for_identicals():    # test for identical angles
    assert not is_angle_between(30, 30, 30)


def test_for_bigger_angles():    # test for angles that lie in the third and fourth quadrent
    assert is_angle_between(181, 270, 359)
