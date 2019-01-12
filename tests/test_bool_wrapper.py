from pytest import fixture, mark

from bool_wrapper import BoolWrapper


@fixture
def wrapped_true():
    return BoolWrapper(value=True)


@fixture
def wrapped_false():
    return BoolWrapper(value=False)


@mark.parametrize('expected_bool', [True, False])
def test_init_sets_correct_value(expected_bool):
    bool_wrapper = BoolWrapper(value=expected_bool)

    assert bool_wrapper._value is expected_bool


@mark.parametrize('not_a_bool, expected_bool', [('a', True), ('', False)])
def test_init_sets_correct_value_when_wrapping_not_a_bool(not_a_bool, expected_bool):
    bool_wrapper = BoolWrapper(value=not_a_bool)

    assert bool_wrapper._value is expected_bool


@mark.parametrize('expected_bool', [True, False])
def test_set_changes_value_to_correct_one(expected_bool):
    bool_wrapper = BoolWrapper(value=not expected_bool)
    bool_wrapper.set(value=expected_bool)

    assert bool_wrapper._value is expected_bool


@mark.parametrize('not_a_bool, expected_bool', [('a', True), ('', False)])
def test_set_changes_value_to_correct_one_when_setting_not_a_bool(not_a_bool, expected_bool):
    bool_wrapper = BoolWrapper(value=not expected_bool)
    bool_wrapper.set(value=not_a_bool)

    assert bool_wrapper._value is expected_bool


def test_bool_representation_of_wrapped_true_is_true(wrapped_true):
    assert wrapped_true
    assert bool(wrapped_true) is True


def test_bool_representation_of_wrapped_false_is_false(wrapped_false):
    assert not wrapped_false
    assert bool(wrapped_false) is False


def test_str_representation_of_wrapped_true_is_same_as_str_representation_of_true(wrapped_true):
    assert str(wrapped_true) == str(True)
    assert repr(wrapped_true) == repr(True)


def test_str_representation_of_wrapped_false_is_same_as_str_representation_of_false(wrapped_false):
    assert str(wrapped_false) == str(False)
    assert repr(wrapped_false) == repr(False)


@mark.xfail(strict=True)
def test_wrapped_true_acts_like_bool_object_in_is_comparison(wrapped_true):
    assert wrapped_true is True


@mark.xfail(strict=True)
def test_wrapped_false_acts_like_bool_object_in_is_comparison(wrapped_false):
    assert wrapped_false is False


def test_wrapped_true_acts_like_bool_object_in_equality_comparison(wrapped_true):
    assert wrapped_true == True
    assert not wrapped_true == False
    assert not wrapped_true == 'a'
    assert not wrapped_true == ''


def test_wrapped_false_acts_like_bool_object_in_equality_comparison(wrapped_false):
    assert wrapped_false == False
    assert not wrapped_false == True
    assert not wrapped_false == 'a'
    assert not wrapped_false == ''


def test_wrapped_true_acts_like_bool_object_in_inequality_comparison(wrapped_true):
    assert wrapped_true != False
    assert not wrapped_true != True
    assert wrapped_true != 'a'
    assert wrapped_true != ''


def test_wrapped_false_acts_like_bool_object_in_inequality_comparison(wrapped_false):
    assert wrapped_false != True
    assert not wrapped_false != False
    assert wrapped_false != 'a'
    assert wrapped_false != ''
