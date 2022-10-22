pin_states = {}

class PinState:

    def __init__(self, parent, freq=None):
        self.parent = parent
        self.freq = freq
        if freq == None:
            self.state = False
        else:
            self.state = 0.0

    def __str__(self):
        if self.freq == None:
            return 'HIGH' if self.state else 'LOW'
        else:
            return f'PWM {100*self.state:.1f}% ({self.freq}Hz)'

    def ChangeFrequency(self, freq):
        self.freq = freq
        self.parent.update()

    def start(self, duty_int):
        self.state = duty_int / 100
        self.parent.update()
    
    def stop(self):
        self.state = 0.0
        self.parent.update()

class MockGpio:

    IN  = 'IN'
    OUT = 'OUT'
    BCM = 'BCM'

    def setmode(self, _):
        pass

    def cleanup(self):
        pass

    def setup(self, pin, mode):
        if mode == self.OUT:
            pin_states[pin] = PinState(self)
        self.update()

    def PWM(self, pin, freq):
        pin_states[pin] = PinState(self, freq)
        self.update()
        return pin_states[pin]

    def output(self, pin, state):
        pin_states[pin].freq = None
        pin_states[pin].state = state
        self.update()

    def update(self):
        for pin, state in pin_states.items():
            print(f'{pin:3}: {state}')
        print()