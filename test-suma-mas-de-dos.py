from sumar import sumar

def test_mas_de_dos_numeros():
    assert sumar("1,2,3,4") == 10
    assert sumar("5,6,7") == 18
    assert sumar("10,20,30,40") == 100