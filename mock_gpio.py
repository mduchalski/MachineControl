# Quick and dirty "mock" GPIO implementation to enable testing w/o actual HW
# TODO Capture pin status instead of just printing function calls

class Callable:

    def __init__(self, name):
        self.name = name

    def __call__(self, *args):
        print(self.name, args)
        # Returning self to enable recursive calls (for PWM)
        return self

    def __getattr__(self, name):
        return Callable(self.name + '.' + name)
        
class MockGpio:

    def __getattr__(self, name):
        if name.isupper() and name != 'PWM':
            # Constants - IN, OUT, BCM, ...
            return name
        else:
            # Methods - setmode, ...
            return Callable(name)
