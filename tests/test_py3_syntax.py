from .tests import check, skip_before


@skip_before((3, 5))
def test_MatMult():
    check('a @ b')
    check('(a * b) @ c')
    check('a * (b @ c)')
    check('a + (b @ c)')


@skip_before((3, 5))
def test_AsyncFunctionDef():
    check('''
async def f(a, b):
    pass
''')


@skip_before((3, 0))
def test_annotations():
    # TODO test precedence
    check('''
def f(a: int, b: str) -> float:
    pass
''')


@skip_before((3, 0))
def test_class_keywords():
    check('''
class Foo(a=3):
    pass
''')
    check('''
class WithMeta(metaclass=type):
    pass
''')


@skip_before((3, 5))
def test_AsyncFor():
    check('''
async def f(y):
    async for x in y:
        pass
''')


@skip_before((3, 0))
def test_py3_with():
    check('''
with a as b:
    pass
''')
    check('''
with a as b, c as d:
    pass
''')
    check('''
with a as b:
    with c as d:
        pass
''')


@skip_before((3, 5))
def test_async_with():
    check('''
async def f(a):
    async with a as b:
        pass
''')


@skip_before((3, 0))
def test_raise_with_cause():
    check('''
raise e from ee
''')


@skip_before((3, 0))
def test_Nonlocal():
    check('''
def f(x):
    nonlocal y
''')
    check('''
def f(x):
    nonlocal y, z
''')


@skip_before((3, 5))
def test_Await():
    check('''
async def f(x):
    await x
''')
    check('''
async def f(x):
    1 + await x
''')
    check('''
async def f(x):
    x = await x
''')
    check('''
async def f(x):
    x += await x
''')
    check('''
async def f(x):
    return 3, (await x)
''')


@skip_before((3, 0))
def test_YieldFrom():
    check('yield from x')
    check('1 + (yield from x)')
    check('x = yield from x')
    check('x += yield from x')
    check('return 3, (yield from x)')


@skip_before((3, 6))
def test_FormattedValue():
    # TODO more
    check('f"a"')


@skip_before((3, 0))
def test_Bytes():
    check('b"a"')


@skip_before((3, 0))
def test_NameConstant():
    check('True')


@skip_before((3, 0))
def test_Starred():
    check('a, *b = 3')
    check('[a, *b]')


@skip_before((3, 0))
def test_kwonlyargs():
    check('def f(a, *, b=3): pass')
    check('def f(a, *args, b=3): pass')
    check('def f(a, *args, b=3, **kwargs): pass')

