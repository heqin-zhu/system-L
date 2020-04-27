import sympy
from system_L import system_L, formula
from random import randint


def random_prop(prop=formula([sympy.Symbol('p')]),
                symbols=sympy.symbols('p q r s t'), n=10):
    fs = [formula([i]) for i in symbols]

    def addLevel(p, sig):
        if sig == 0:
            return non(p)
        else:
            cur = fs[randint(0, len(fs)-1)]
            if randint(0, 1) == 0:
                return contain(cur, p)
            else:
                return contain(p, cur)
    for i in range(10):
        prop = addLevel(prop, randint(0, 1))
    return prop


def test_systemL():
    L = system_L()
    props = [('((x1>(x2>x3))>(x1> x2)) ->((x1>(x2>x3))->(x1>x3))', []),
             ('(~(x1>x3)>x1)', []),
             ('p->r', ['p->q', '~(q->r)->~p']),
             ('p>(~q>~(p>q))', []),
             ('p>q>p>p', []),
             ('~p>p>p', []),
             ('~(p>q)>~q', []),
             ('~(p>q)>~q', []),
             ]
    for prop, garma in props:
        L.prove(garma, prop)


if __name__ == "__main__":
    test_systemL()
