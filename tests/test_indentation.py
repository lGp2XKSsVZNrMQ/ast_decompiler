from .tests import assert_decompiles


def test_indentation():
    assert_decompiles('''
if x:
    pass
''', '''if x:
 pass
''', indentation=1)


def test_starting_indentation():
    assert_decompiles('''3''', '''    3
''', starting_indentation=4, do_check=False)
