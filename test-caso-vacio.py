import pytest
from sumar import sumar

def test_suma_string_vacio_devuelve_cero():
    assert sumar("") == 0
