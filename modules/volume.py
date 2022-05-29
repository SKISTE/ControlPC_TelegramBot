from modules.refences.sound import Sound


def volume(num):
    if int(num) > 100 or int(num) < 0:
        return Exception('Incorrect number')
    else:
        Sound.volume_set(int(num))
        return f'Громкость музыки успешно поставлена на {str(num)}'


def get_current_volume():
    return str(Sound.current_volume())


def volup():
    Sound.volume_up()
    return


def voldown():
    Sound.volume_down()
    return
