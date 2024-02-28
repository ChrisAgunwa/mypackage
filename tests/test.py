from mypackage import myModule

def test_top_n():
    """
    makes sure top_n works correctly
    """
    assert myModule.top_n([8, 4, 7, 2, 1, 6], 3) == [8, 7, 6], 'incorret'
    assert myModule.top_n([10, 1, 12, 9, 2], 2) == [12, 10], 'incorrect'
    assert myModule.top_n([1, 2, 3, 4, 5], 5) == [5,4,3,2,1], 'incorrect'



