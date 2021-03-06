import gtable as gt
import numpy as np
import pytest


def test_required_column_present():
    d = {'A': [1, 2, 3, 4], 'B': [2.2, 1.5, 7.3, 2.6]}
    t = gt.Table(d)
    with pytest.raises(KeyError):
        t.required_column('B', np.dtype(('U', 10)))


def test_str_alternative():
    d = {'A': [1, 2, 3, 4], 'B': [2.2, 1.5, 7.3, 2.6]}
    t = gt.Table(d)
    t.required_column('C', np.dtype(('U', 10)))
    t.fill_column('C', 'hello')
    assert np.all(t.C.values == np.array(['hello', 'hello', 'hello', 'hello'], dtype=np.dtype(('U', 10))))


