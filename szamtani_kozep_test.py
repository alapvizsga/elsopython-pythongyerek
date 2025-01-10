import py1
def test_szamtani_kozep():
    assert py1.szamtani_kozep(1, 3) == 2
    assert py1.szamtani_kozep(10, 30) == 20
    assert py1.szamtani_kozep(1, 100) == 50.5
    assert py1.szamtani_kozep(1, 101) == 51
    assert py1.szamtani_kozep(1, 102) == 51.5
    assert py1.szamtani_kozep(1, 103) == 52
    
