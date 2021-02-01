import time


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = ended_at - started_at
        print(f'Функция работала {elapsed:.4f} секунд(ы)')
        return result

    return surrogate
