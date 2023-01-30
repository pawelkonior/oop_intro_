class Auto:
    def __init__(self, model, max_speed):
        self.model = model
        self.speed = 0
        self.max_speed = max_speed
        self.engine = False

    def start_engine(self):
        if not self.engine:
            self.engine = True
            print('Silnik odpalony')
        else:
            print('Silnik już był odpalony')

    def stop_engine(self):
        if self.speed == 0:
            self.engine = False
            print('Silnik zgaszony')
        else:
            print('Zatrzymaj wpierw auto! ⛔️')

    def speed_up(self, amount):
        if self.engine:
            self.speed = min(self.speed + amount, self.max_speed)
            print(f'Jedziesz z prędkością {self.speed}')
        else:
            print('Odpal silnik wpierw')

    def slow_down(self, amount):
        self.speed = max(self.speed - amount, 0)
        print(f'Jedziesz z prędkością {self.speed}')


bmw = Auto('e46', 160)
fiat = Auto('tipo', 240)

bmw.speed_up(200)
bmw.start_engine()
bmw.speed_up(40)
bmw.speed_up(60)
bmw.speed_up(500)
bmw.stop_engine()
bmw.slow_down(20)
bmw.slow_down(40)
bmw.slow_down(500)
bmw.stop_engine()
