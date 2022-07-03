import serial


on = b"\xA0\x01\x01\xA2"
off = b"\xA0\x01\x00\xA1"


class _Simulator:
    def __init(self):
        pass

    def close(self):
        pass

    def write(self, data):
        pass


class Switcher:
    def __init__(self, port, debug=False):
        if port == "Simulator":
            self.ser = _Simulator()
            self.debug = True
        else:
            self.ser = serial.Serial(port, 9600, timeout=2)
            self.debug = debug
        self.is_on = False

    def _talk(self):
        if self.debug:
            print(f"Switcher is {self.is_on}")

    def close(self):
        self.ser.close()

    def switch_on(self):
        self.is_on = True
        self.ser.write(on)
        self._talk()

    def switch_off(self):
        self.is_on = False
        self.ser.write(off)
        self._talk()

    def toggle(self):
        if self.is_on:
            self.switch_off()
        else:
            self.switch_on()
