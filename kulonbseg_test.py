import py1
def test_kulonbseg():
    assert py1.kulonbseg(3, 2) == 1
    assert py1.kulonbseg(2, 3) == -1
    assert py1.kulonbseg(0, 0) == 0
    assert py1.kulonbseg(0, 1) == -1
    assert py1.kulonbseg(1, 0) == 1
    assert py1.kulonbseg(1, 1) == 0
    assert py1.kulonbseg(1, 2) == -1
    assert py1.kulonbseg(2, 1) == 1
    assert py1.kulonbseg(2, 2) == 0
    assert py1.kulonbseg(2, 4) == -2
    assert py1.kulonbseg(4, 2) == 2
 
  
