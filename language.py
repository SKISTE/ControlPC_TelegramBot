class RU:
    def __init__(self):
        print('Русский язык загружен')

    LANG = 'RU'
    error = 'Произошла непредвиденная ошибка:'
    volume = 'Громкость: '
    change_volume_percent = 'Изменить громкость по процентам: '
    volume_set = 'Громкость поставлена на '
    pong = 'Понг блять'
    change_volume = 'Изменить громкость: '
    pc_shutdown = 'Пк выключится через '
    minute = 'минут'
    remove_pc_shutdown = 'План выключения пк удален'
    help = '''Worked:
/pause - Вкл/выкл музыку
/громкость - Изменить громкость винды
/след - Следующий трек
/prevtrack - Предыдущий трек
/screen - Скрин экрана
/ping - Проверка работоспособности
/games - Список игр
/start *номер* - запустить игру по номеру из списка /games
/shutdown *min* - Выключить пк через min минут'''
    started = 'Запустили '
    nexttrack = 'Трек переключен на следующий'
    prevtrack = 'Трек переключен на предыдущий'
    pausemusic = 'Трек остановлен/возобновлен'


class EN:
    def __init__(self):
        print('English lang loaded')

    LANG = 'EN'
    error = 'An unexpected error has occurred:'
    volume = 'Volume: '
    change_volume_percent = 'Change volume by percentage: '
    volume_set = 'Volume set '
    pong = 'Pong'
    change_volume = 'Change volume: '
    pc_shutdown = 'PC turns off after '
    minute = 'minutes'
    remove_pc_shutdown = 'PC shutdown plan deleted'
    help = '''Worked:
/pause - Play/pause music
/volume - Change windows volume
/nexttrack - Next track
/prevtrack - Prev track
/screen - Screenshot
/ping - Check
/games - Games list
/start *num* - Start game on number from /games
/shutdown *min* - Shutdown pc after *min*'''
    started = 'Started '
    nexttrack = 'Track switched to next'
    prevtrack = 'Track switched to previous'
    pausemusic = 'Track stopped/resume'
