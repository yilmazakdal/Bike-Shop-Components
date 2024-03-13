from src.components import (Gears,Chain,Brakes)
class ServicePerson:
    def __init__(self, bike):
        self.bike=bike
    def order_parts(self):
        if self.bike.bell.current_state==0:
            self.bike.bell.current_state=self.bike.bell.max_lifespan
        if self.bike.brakes.current_state==0:
            self.bike.brakes.current_state=self.bike.brakes.max_lifespan
        if self.bike.tyres.current_state==0:
            self.bike.tyres.current_state=self.bike.tyres.max_lifespan
        if self.bike.chain.current_state==0:
            self.bike.chain.current_state=self.bike.chain.max_lifespan
        if self.bike.gears.current_state==0:
            self.bike.gears.current_state=self.bike.gears.max_lifespan
        if self.bike.frame.current_state==0:
            self.bike.frame.current_state=self.bike.frame.max_lifespan
    
    def service_parts(self):
        if self.bike.bell.current_state > 0 and self.bike.bell.current_state <self.bike.bell.max_lifespan/4:
            self.bike.bell.current_state = self.bike.bell.max_lifespan * 0.6
            self.bike.bell.check_condition()
        if self.bike.brakes.current_state > 0 and self.bike.brakes.current_state <self.bike.brakes.max_lifespan/4:
            self.bike.brakes.current_state = self.bike.brakes.max_lifespan * 0.6
            self.bike.brakes.check_condition()
        if self.bike.chain.current_state > 0 and self.bike.chain.current_state <self.bike.chain.max_lifespan/4:
            self.bike.chain.current_state = self.bike.chain.max_lifespan * 0.6
            self.bike.chain.check_condition()
        if self.bike.tyres.current_state > 0 and self.bike.tyres.current_state <self.bike.tyres.max_lifespan/4:
            self.bike.tyres.current_state = self.bike.chain.max_lifespan * 0.6
            self.bike.tyres.check_condition()
        if self.bike.gears.current_state > 0 and self.bike.gears.current_state <self.bike.gears.max_lifespan/4:
            self.bike.gears.current_state = self.bike.gears.max_lifespan * 0.6
            self.bike.gears.check_condition()
        if self.bike.frame.current_state > 0 and self.bike.frame.current_state <self.bike.frame.max_lifespan/4:
            self.bike.frame.current_state = self.bike.frame.max_lifespan * 0.6
            self.bike.frame.check_condition()
     
    def oil(self):
        if isinstance(self.bike.chain,Chain) and isinstance(self.bike.brakes,Brakes) and isinstance(self.bike.gears,Gears):
            if self.bike.brakes.current_state > self.bike.brakes.max_lifespan/2:
                self.bike.brakes.current_state = self.bike.brakes.max_lifespan
                self.bike.brakes.check_condition()
            if self.bike.chain.current_state > self.bike.chain.max_lifespan/2:
                self.bike.chain.current_state = self.bike.chain.max_lifespan
                self.bike.chain.check_condition()
            if self.bike.gears.current_state > self.bike.gears.max_lifespan/2:
                self.bike.gears.current_state = self.bike.gears.max_lifespan
                self.bike.gears.check_condition()
        else:
            raise TypeError('Your bike is missing one or more components to oil!')

    def clean(self):
        if self.bike.frame.component_state == 'Good':
            self.bike.frame.current_state = self.bike.frame.max_lifespan
            self.bike.frame.check_condition()
    
    def pump_wheels(self):
        if self.bike.tyres.component_state == 'Good':
            self.bike.tyres.current_state = self.bike.tyres.max_lifespan
            self.bike.tyres.check_condition()

    def service_bike(self):
        self.service_parts()
        self.oil()
        self.pump_wheels()
        self.clean()

    def check_safety(self):
        self.bike.ring_bell()
        if self.bike.brakes.component_state == 'Good' or self.bike.brakes.component_state=='Pristine':
            return "Your bike is safe for now.Good to go..."
        else:
            return "You need to visit a bike shop asap..."
    
    def check_up(self):
        list_of_broken_parts = [self.bike.bell.component_state=='Broken',self.bike.brakes.component_state=='Broken',self.bike.chain.component_state=='Broken',self.bike.frame.component_state=='Broken',self.bike.gears.component_state=='Broken',self.bike.tyres.component_state=='Broken']

        list_of_fragile_parts = [self.bike.bell.component_state=='Fragile',self.bike.brakes.component_state=='Fragile',self.bike.chain.component_state=='Fragile',self.bike.frame.component_state=='Fragile',self.bike.gears.component_state=='Fragile',self.bike.tyres.component_state=='Fragile']
       
        if any(list_of_broken_parts):
            self.order_parts()
        elif any(list_of_fragile_parts):
            self.service_parts()
        else:
            self.service_bike()
        self.check_safety()
            


