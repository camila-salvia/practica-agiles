from sumar import sumar

def test_dos_numeros():
    assert sumar("1,2") == 3
    assert sumar("4,2") == 6