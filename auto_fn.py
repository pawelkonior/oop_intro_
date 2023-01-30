# model, speed, max speed, engine
# start engine, stop engine, speed up, slow down

def auto_initializer(model, max_speed):
    return {
        'model': model,
        'speed': 0,
        'max_speed': max_speed,
        'engine': False
    }


def start_engine(car):
    if not car['engine']:
        car['engine'] = True
        print('Silnik odpalony')
    else:
        print('Silnik już był odpalony')


def stop_engine(car):
    if car['speed'] == 0:
        car['engine'] = False
        print('Silnik zgaszony')
    else:
        print('Zatrzymaj wpierw auto! ⛔️')


def speed_up(car, amount):
    if car['engine']:
        car['speed'] = min(car['speed'] + amount, car['max_speed'])
        print(f'Jedziesz z prędkością {car["speed"]}')
    else:
        print('Odpal silnik wpierw')


def slow_down(car, amount):
    car['speed'] = max(car['speed'] - amount, 0)
    print(f'Jedziesz z prędkością {car["speed"]}')


bmw = auto_initializer('e46', 160)
fiat = auto_initializer('tipo', 240)

speed_up(bmw, 200)
start_engine(bmw)
speed_up(bmw, 40)
speed_up(bmw, 60)
speed_up(bmw, 500)
stop_engine(bmw)
slow_down(bmw, 20)
slow_down(bmw, 40)
slow_down(bmw, 500)
stop_engine(bmw)
