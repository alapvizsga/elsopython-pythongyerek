import py1
def test_kocka_terfogat():
    assert py1.kocka_terfogat(1) == 1
    assert py1.kocka_terfogat(2) == 8
    assert py1.kocka_terfogat(3) == 27
    assert py1.kocka_terfogat(4) == 64
    assert py1.kocka_terfogat(5) == 125
    assert py1.kocka_terfogat(6) == 216
    assert py1.kocka_terfogat(7) == 343
    assert py1.kocka_terfogat(8) == 512
    assert py1.kocka_terfogat(9) == 729
    assert py1.kocka_terfogat(10) == 1000
    assert py1.kocka_terfogat(11) == 1331
    assert py1.kocka_terfogat(12) == 1728
    assert py1.kocka_terfogat(13) == 2197
    
