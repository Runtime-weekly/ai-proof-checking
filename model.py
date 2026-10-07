"""Exact arithmetic used by the original RUNTIME proof-checking illustrations."""
from math import isqrt

def polynomial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError('n must be a nonnegative integer')
    return n*n+n+41

def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))

def checks():
    rows=[{'n':n,'value':polynomial(n),'prime':is_prime(polynomial(n))} for n in range(41)]
    assert all(row['prime'] for row in rows[:40])
    assert rows[40]['value']==41*41 and not rows[40]['prime']
    assert not is_prime(1) and is_prime(2) and not is_prime(4)
    for a in range(20):
        for b in range(20):
            assert 2*a+2*b==2*(a+b)
    return rows

if __name__=='__main__':
    import json
    print(json.dumps(checks(),indent=2))
