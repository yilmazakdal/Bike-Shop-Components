from src.service_person import (ServicePerson)
from src.bikes import (Bike, BMX, Mountain, Street, Racing)
from src.components import (Bell,Brakes,Chain,Tyres,Gears,Frame)
import pytest

def test_order_parts_replaces_broken_bell():
    bell=Bell(0,100)
    tyres=Tyres(100,100)
    brakes=Brakes(99,100)
    chain=Chain(80,100)
    gears=Gears(80,100)
    frame=Frame(100,100)
    bike=Bike(bell,brakes,chain,tyres,gears,frame)
    service_person=ServicePerson(bike)
    assert bell.current_state==0
    service_person.order_parts()
    assert bell.current_state==100
def test_order_parts_replaces_broken_chain():
    bell=Bell(90,100)
    tyres=Tyres(100,100)
    brakes=Brakes(99,100)
    chain=Chain(0,100)
    gears=Gears(90,100)
    frame=Frame(100,100)
    bike=Bike(bell,brakes,chain,tyres,gears,frame)
    service_person=ServicePerson(bike)
    assert chain.current_state==0
    service_person.order_parts()
    assert chain.current_state==100
def test_order_parts_replaces_broken_brakes():
    bell=Bell(90,100)
    tyres=Tyres(100,100)
    brakes=Brakes(0,100)
    chain=Chain(100,100)
    gears=Gears(0,100)
    frame=Frame(100,100)
    bike=Bike(bell,brakes,chain,tyres,gears,frame)
    service_person=ServicePerson(bike)
    assert brakes.current_state==0
    service_person.order_parts()
    assert brakes.current_state==100
def test_order_parts_replaces_broken_tyres():
    bell=Bell(90,100)
    tyres=Tyres(0,100)
    brakes=Brakes(0,100)
    chain=Chain(100,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    bike=Bike(bell,brakes,chain,tyres,gears,frame)
    service_person=ServicePerson(bike)
    assert tyres.current_state==0
    service_person.order_parts()
    assert tyres.current_state==100
def test_service_parts_replaces__brakes_from_fragile_to_good():
    bell=Bell(90,100)
    tyres=Tyres(90,100)
    brakes=Brakes(20,100)
    chain=Chain(100,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    bike=Bike(bell,brakes,chain,tyres,gears,frame)
    service_person=ServicePerson(bike)
    assert brakes.current_state==20
    assert brakes.component_state == 'Fragile'
    service_person.service_parts()
    assert brakes.current_state== 60
    assert brakes.component_state == 'Good'
def test_service_parts_replaces__chain_from_fragile_to_good():
    bell=Bell(90,100)
    tyres=Tyres(90,100)
    brakes=Brakes(100,100)
    chain=Chain(20,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    bike=Bike(bell,brakes,chain,tyres,gears,frame)
    service_person=ServicePerson(bike)
    assert chain.current_state==20
    assert chain.component_state == 'Fragile'
    service_person.service_parts()
    assert chain.current_state== 60
    assert chain.component_state == 'Good'
def test_service_parts_replaces__tyres_from_fragile_to_good():
    bell=Bell(90,100)
    tyres=Tyres(20,100)
    brakes=Brakes(100,100)
    chain=Chain(100,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    bike=Bike(bell,brakes,chain,tyres,gears,frame)
    service_person=ServicePerson(bike)
    assert tyres.current_state==20
    assert tyres.component_state == 'Fragile'
    service_person.service_parts()
    assert tyres.current_state== 60
    assert tyres.component_state == 'Good'
def test_oil_replaces__brakes_from_good_to_pristine():
    bell=Bell(90,100)
    tyres=Tyres(90,100)
    brakes=Brakes(60,100)
    chain=Chain(100,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    bike=Bike(bell,brakes,chain,tyres,gears,frame)
    service_person=ServicePerson(bike)
    assert brakes.current_state==60
    assert brakes.component_state == 'Good'
    service_person.oil()
    assert brakes.current_state==100
    assert brakes.component_state == 'Pristine'
def test_oil_replaces__chain_from_good_to_pristine():
    bell=Bell(90,100)
    tyres=Tyres(90,100)
    brakes=Brakes(90,100)
    chain=Chain(70,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    bike=Bike(bell,brakes,chain,tyres,gears,frame)
    service_person=ServicePerson(bike)
    assert chain.current_state==70
    assert chain.component_state == 'Good'
    service_person.oil()
    assert chain.current_state==100
    assert chain.component_state == 'Pristine'
def test_oil_replaces__gears_from_good_to_pristine():
    bell=Bell(90,100)
    tyres=Tyres(90,100)
    brakes=Brakes(90,100)
    chain=Chain(70,100)
    gears=Gears(55,100)
    frame=Frame(100,100)
    bike=Bike(bell,brakes,chain,tyres,gears,frame)
    service_person=ServicePerson(bike)
    assert gears.current_state==55
    assert gears.component_state == 'Good'
    service_person.oil()
    assert gears.current_state==100
    assert gears.component_state == 'Pristine'

def test_oil_throws_error_if_brakes_chain_or_gears_are_the_wrong_components():
    with pytest.raises(TypeError, match=r'Your bike is missing one or more components to oil!'):
        bell=Bell(90,100)
        tyres=Tyres(90,100)
        brakes=''
        chain=Chain(70,100)
        gears=Gears(55,100)
        frame=Frame(100,100)
        bike=Bike(bell,brakes,chain,tyres,gears,frame)
        service_person=ServicePerson(bike)
        assert gears.current_state==55
        assert gears.component_state == 'Good'
        service_person.oil()
        assert gears.current_state==100
        assert gears.component_state == 'Pristine'
def test_clean_frame_from_good_to_pristine():
    bell=Bell(90,100)
    tyres=Tyres(90,100)
    brakes=Brakes(90,100)
    chain=Chain(70,100)
    gears=Gears(55,100)
    frame=Frame(55,100)
    bike=Bike(bell,brakes,chain,tyres,gears,frame)
    service_person=ServicePerson(bike)
    assert frame.current_state==55
    assert frame.component_state == 'Good'
    service_person.clean()
    assert frame.current_state==100
    assert frame.component_state == 'Pristine'
def test_pump_wheels_tyres_from_good_to_pristine():
    bell=Bell(90,100)
    tyres=Tyres(55,100)
    brakes=Brakes(90,100)
    chain=Chain(70,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    bike=Bike(bell,brakes,chain,tyres,gears,frame)
    service_person=ServicePerson(bike)
    assert tyres.current_state==55
    assert tyres.component_state == 'Good'
    service_person.pump_wheels()
    assert tyres.current_state==100
    assert tyres.component_state == 'Pristine'
def test_check_safety_of_bike_ringing_bell_and_checking_brakes():
    bell=Bell(90,100)
    tyres=Tyres(55,100)
    brakes=Brakes(40,100)
    chain=Chain(70,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    bike=Bike(bell,brakes,chain,tyres,gears,frame)
    service_person=ServicePerson(bike)
    result = 'You need to visit a bike shop asap...'
    assert result == service_person.check_safety()
def test_check_up():
    bell=Bell(0,100)
    tyres=Tyres(90,100)
    brakes=Brakes(90,100)
    chain=Chain(90,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    bike=Bike(bell,brakes,chain,tyres,gears,frame)
    service_person=ServicePerson(bike)
    service_person.check_up()
    assert service_person.bike.bell.component_state == 'Pristine'
def test_check_up():
    bell=Bell(90,100)
    tyres=Tyres(90,100)
    brakes=Brakes(90,100)
    chain=Chain(20,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    bike=Bike(bell,brakes,chain,tyres,gears,frame)
    service_person=ServicePerson(bike)
    service_person.check_up()
    assert service_person.bike.chain.component_state == 'Good'

    
