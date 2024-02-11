from Calendario import Dia
def test_calendario():
    calendario=Dia()

    assert calendario.dia==1
    assert calendario.mes==1
    assert calendario.año==1970
    assert calendario.dia_semana==3
    assert calendario.info()=='Jueves, 1 de enero de 1970'

def test_de_num_a_mes():
    Calendario=Dia(23,3,1956)

    assert Calendario.de_num_a_mes()=='marzo'

def test_calcular_dia_semana():
    Calendario=Dia(20,2,1957)

    #assert Calendario.calcular_dia_semana(25,3,1956)==0
    assert Calendario.calcular_dia_semana()=='Jueves'

def test_dia_a_verificar():
    Calendario=Dia(30,2,1956)

    assert Calendario.dia_a_verificar()==False







