import sympy
from system_L import *


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
             (str(random_prop(n=5)), []),
             (str(random_prop(n=10)), []),
             ('invalid', []),
             ]
    for prop, garma in props:
        try:
            L.prove(garma, prop)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    test_systemL()
