from src.components import(Bell)

class BrokenBikeError(Exception):
    pass

class Bike:
    def __init__(self,bell,brakes,chain,tyres,gears,frame):
        self.bell = bell
        self.brakes =brakes
        self.chain=chain
        self.tyres=tyres
        self.gears=gears
        self.frame=frame
        self.bell_usage_rate=1
        self.brakes_usage_rate=1
        self.chain_usage_rate=1
        self.tyres_usage_rate=1
        self.gears_usage_rate=1
        self.frame_usage_rate=1
    
    def ride(self):
        list_conditions_broken=[self.bell.check_condition(),self.brakes.check_condition(),self.chain.check_condition(),self.tyres.check_condition(),self.gears.check_condition(),self.frame.check_condition()]
        if all(list_conditions_broken): #This evaluates to true if all components are working
            list_conditions_good_or_pristine=[self.bell.check_condition()>=self.bell.max_lifespan/2,self.brakes.check_condition()>=self.brakes.max_lifespan/2,self.chain.check_condition()>=self.chain.max_lifespan/2,self.tyres.check_condition()>=self.tyres.max_lifespan/2,self.gears.check_condition()>=self.gears.max_lifespan/2,self.frame.check_condition()>=self.frame.max_lifespan/2]
            if all(list_conditions_good_or_pristine): 
                print('Your ride is good or pristine!')
            else:
                print('Your ride is poor or fragile!')
            self.bell.current_state -= self.bell_usage_rate
            self.brakes.current_state -= self.brakes_usage_rate
            self.chain.current_state -= self.chain_usage_rate
            self.tyres.current_state -= self.tyres_usage_rate
            self.gears.current_state -= self.gears_usage_rate
            self.frame.current_state -= self.frame_usage_rate
        else: #Enters here if any component is broken
            raise BrokenBikeError('Some components are broken! You cannot ride this bike!')

    def ring_bell(self):
        if isinstance(self.bell,Bell):
            list_conditions_broken=[self.bell.check_condition(),self.brakes.check_condition(),self.chain.check_condition(),self.tyres.check_condition(),self.gears.check_condition(),self.frame.check_condition()]
            if all(list_conditions_broken): 
                list_conditions_good_or_pristine=[self.bell.check_condition()>=self.bell.max_lifespan/2,self.brakes.check_condition()>=self.brakes.max_lifespan/2,self.chain.check_condition()>=self.chain.max_lifespan/2,self.tyres.check_condition()>=self.tyres.max_lifespan/2,self.gears.check_condition()>=self.gears.max_lifespan/2,self.frame.check_condition()>=self.frame.max_lifespan/2]
                if all(list_conditions_good_or_pristine): 
                    print('Ring! Ring! Ring!')
                else:
                    print('Ring! cling...')
            else: 
                print('The bell fell off!')
        else:
            raise TypeError('Your bike is missing a bell!')

class Racing(Bike):
    def __init__(self,bell,brakes,chain,tyres,gears,frame):
        super().__init__(bell,brakes,chain,tyres,gears,frame)
        self.chain_usage_rate=1.05
        self.tyres_usage_rate=1.05

class BMX(Bike):
    def __init__(self,bell,brakes,chain,tyres,gears,frame):
        super().__init__(bell,brakes,chain,tyres,gears,frame)
        # self.brakes.current_state=10
        # self.brakes.max_lifespan=10
        self.brakes_usage_rate=0
        self.tyres_usage_rate=1.15

class Mountain(Bike):
    def __init__(self,bell,brakes,chain,tyres,gears,frame):
        super().__init__(bell,brakes,chain,tyres,gears,frame)
        self.chain_usage_rate=0.85

class Street(Bike):
    def __init__(self,bell,brakes,chain,tyres,gears,frame):
        super().__init__(bell,brakes,chain,tyres,gears,frame)
        self.brakes_usage_rate=1.05