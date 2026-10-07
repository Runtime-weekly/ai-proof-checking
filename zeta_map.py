"""Recompute the four numerical points used in the video. Does not prove RH.

Optional dependency: mpmath. Does not change the four Lean control tests.
"""
import json
import mpmath as mp

mp.mp.dps = 40
points = []
for index in range(1, 5):
    value = mp.zetazero(index)
    residual = abs(mp.zeta(value))
    assert residual < mp.mpf('1e-35')
    points.append({
        'index': index,
        'real': str(value.real),
        'imaginary': str(value.imag),
        'residual': str(residual),
    })
print(json.dumps({
    'points': points,
    'decimal_digits': 40,
    'limits': 'Numerical examples, not a proof about all zeros or verification of the OpenAI research claim.',
}, indent=2))
