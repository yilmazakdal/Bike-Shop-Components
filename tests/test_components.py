from src.components import (Component,Bell,Brakes,Chain,Tyres)

def test_returns_when_max_lifespan_is_0():
    expected = 0
    chain=Component(60,0)
    result = chain.check_condition()
    print(f'Result is: {result}')
    assert result == expected
def test_returns_when_max_lifespan_is_bigger_than_current_state():
    expected = 60
    chain=Component(60,100)
    result = chain.check_condition()
    print(f'Result is: {result}')
    assert result == expected
def test_bell():
    expected = 60
    bell=Bell(60,100)
    result = bell.check_condition()
    print(f'Result is: {result}')
    assert result == expected
def test_bell_uses_the_bell_method():
    expected = 'Use the bell Ring! Ring!'
    bell=Bell(60,100)
    result = bell.use_bell()
    print(f'Result is: {result}')
    assert result == expected
def test_bell_uses_the_bell_method():
    expected = 'You can not use the component!'
    bell=Bell(0,100)
    result = bell.use_bell()
    print(f'Result is: {result}')
    assert result == expected
def test_bell_uses_the_bell_method():
    expected = 'Do not forget changing the tyres for winter conditions.'
    bell=Tyres(30,50)
    result = bell.use_tyres()
    print(f'Result is: {result}')
    assert result == expected