from src.components import (Bell,Brakes,Chain,Tyres,Gears,Frame)
from src.bikes import (Bike, Racing, BMX, Mountain,Street,BrokenBikeError)
import pytest

def test_returns_pristine_message_if_all_components_are_good_or_pristine():
    bell=Bell(52,100)
    brakes=Brakes(100,100)
    chain=Chain(100,100)
    tyres=Tyres(99,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    bike=Bike(bell=bell,brakes=brakes,chain=chain,tyres=tyres,frame=frame,gears=gears)
    bike.ride()
    assert bike.bell.current_state==51
    assert bike.brakes.current_state==99
    assert bike.chain.current_state==99
    assert bike.tyres.current_state==98

def test_returns_poor_message_if_one_component_is_fragile():
    bell=Bell(22,100)
    brakes=Brakes(100,100)
    chain=Chain(100,100)
    tyres=Tyres(99,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    bike=Bike(bell=bell,brakes=brakes,chain=chain,tyres=tyres,frame=frame,gears=gears)
    bike.ride()
    assert bike.bell.current_state==21
    assert bike.brakes.current_state==99
    assert bike.chain.current_state==99
    assert bike.tyres.current_state==98

def test_returns_broken_message_if_one_component_is_broken():
    with pytest.raises(BrokenBikeError,match=r'Some components are broken! You cannot ride this bike!'):
        bell=Bell(22,100)
        brakes=Brakes(0,100)
        chain=Chain(100,100)
        tyres=Tyres(99,100)
        gears=Gears(100,100)
        frame=Frame(100,100)
        bike=Bike(bell=bell,brakes=brakes,chain=chain,tyres=tyres,frame=frame,gears=gears)
        bike.ride()
        assert bike.bell.current_state==22
        assert bike.brakes.current_state==0
        assert bike.chain.current_state==100
        assert bike.tyres.current_state==99

def test_ring_returns_Ring_Ring_Ring_message_if_all_components_are_good_or_pristine():
    bell=Bell(52,100)
    brakes=Brakes(100,100)
    chain=Chain(100,100)
    tyres=Tyres(99,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    bike=Bike(bell=bell,brakes=brakes,chain=chain,tyres=tyres,frame=frame,gears=gears)
    bike.ring_bell()

def test_ring_returns_ring_cling_if_any_components_are_poor_or_fragile():
    bell=Bell(26,100)
    brakes=Brakes(100,100)
    chain=Chain(100,100)
    tyres=Tyres(99,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    bike=Bike(bell=bell,brakes=brakes,chain=chain,tyres=tyres,frame=frame,gears=gears)
    bike.ring_bell()

def test_returns_bell_fell_off_message_if_any_component_is_broken():
    bell=Bell(22,100)
    brakes=Brakes(0,100)
    chain=Chain(100,100)
    tyres=Tyres(99,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    bike=Bike(bell=bell,brakes=brakes,chain=chain,tyres=tyres,frame=frame,gears=gears)
    bike.ring_bell()

def test_returns_error_if_bell_not_a_object_of_class_bell():
    with pytest.raises(TypeError,match=r'Your bike is missing a bell!'):
        bell='bell'
        brakes=Brakes(0,100)
        chain=Chain(100,100)
        tyres=Tyres(99,100)
        gears=Gears(100,100)
        frame=Frame(100,100)
        bike=Bike(bell=bell,brakes=brakes,chain=chain,tyres=tyres,frame=frame,gears=gears)
        bike.ring_bell()

def test_racing_bike_wears_tyres_and_chain_more():
    bell=Bell(52,100)
    brakes=Brakes(100,100)
    chain=Chain(100,100)
    tyres=Tyres(99,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    racing=Racing(bell=bell,brakes=brakes,chain=chain,tyres=tyres,frame=frame,gears=gears)
    racing.ride()
    assert racing.bell.current_state==51
    assert racing.brakes.current_state==99
    assert racing.chain.current_state==98.95
    assert racing.tyres.current_state==97.95

def test_BMX_bike_wears_tyres_more_and_does_not_wear_breaks():
    bell=Bell(52,100)
    brakes=Brakes(100,100)
    chain=Chain(100,100)
    tyres=Tyres(99,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    bmx=BMX(bell=bell,brakes=brakes,chain=chain,tyres=tyres,frame=frame,gears=gears)
    bmx.ride()
    assert bmx.bell.current_state==51
    assert bmx.brakes.current_state==100
    assert bmx.chain.current_state==99
    assert bmx.tyres.current_state==97.85

def test_mountain_bike_wears_chain_less():
    bell=Bell(52,100)
    brakes=Brakes(100,100)
    chain=Chain(100,100)
    tyres=Tyres(99,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    mountain=Mountain(bell=bell,brakes=brakes,chain=chain,tyres=tyres,frame=frame,gears=gears)
    mountain.ride()
    assert mountain.bell.current_state==51
    assert mountain.brakes.current_state==99
    assert mountain.chain.current_state==99.15
    assert mountain.tyres.current_state==98

def test_street_bike_wears_brakes_more():
    bell=Bell(52,100)
    brakes=Brakes(100,100)
    chain=Chain(100,100)
    tyres=Tyres(99,100)
    gears=Gears(100,100)
    frame=Frame(100,100)
    street=Street(bell=bell,brakes=brakes,chain=chain,tyres=tyres,frame=frame,gears=gears)
    street.ride()
    assert street.bell.current_state==51
    assert street.brakes.current_state==98.95
    assert street.chain.current_state==99
    assert street.tyres.current_state==98