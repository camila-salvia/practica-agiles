from sumar import sumar

def test_numeros_negativos():
    assert sumar("-1,2") == 1
    assert sumar("3,-2") == 1
    assert sumar("-5,-5") == -10
