class Component:
    def __init__(self,current_state,max_lifespan):
        self.current_state=min(current_state,max_lifespan)
        self.max_lifespan= max_lifespan
        self.check_condition()
    
    def check_condition(self):
        if self.max_lifespan <= 0:
            self.component_state = 'Broken'
        elif self.current_state >= self.max_lifespan:
            self.component_state = 'Pristine'
        elif self.current_state > self.max_lifespan/2:
            self.component_state = 'Good'
        elif self.current_state > self.max_lifespan/4:
            self.component_state = 'Poor'
        elif self.current_state > 0:
            self.component_state = 'Fragile' 
        else:
            self.component_state = 'Broken' 

        print(f'Your component is {self.component_state}')
        return self.current_state

class Bell(Component):

    def use_bell(self):
        if self.check_condition() == 0:
            return 'You can not use the component!'
        else:
            self.current_state -= 1
            return 'Use the bell Ring! Ring!' 


class Brakes(Component):
    def use_brakes(self):
        if self.check_condition() == 0:
            return 'You can not use the component!'
        else:
            self.current_state -= 1
            return 'Do not brakes harshly! Safety first...'

class Chain(Component):
    def use_chain(self):
        if self.check_condition() == 0:
            return 'You can not use the component!'
        else:
            self.current_state -= 1
            return 'Do not forget to oil the chains. Things get dirty...'

class Tyres(Component):
    def use_tyres(self):
        if self.check_condition() == 0:
            return 'You can not use the component!'
        else:
            self.current_state -= 1
            return 'Do not forget changing the tyres for winter conditions.'

class Gears(Component):
    def use_gears(self):
        if self.check_condition() == 0:
            return 'You can not use the component!'
        else:
            self.current_state -= 1
            return 'Do not forget changing the gears before it\'s too late'

class Frame(Component):
    def use_frame(self):
        if self.check_condition() == 0:
            return 'You can not use the component!'
        else:
            self.current_state -= 1
            return 'If you do not change, you will fall!'