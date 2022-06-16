import time


def timer_factory(ns=False):
    """
    ns: Use seconds to count time by default, pass True to use nanoseconds
    """

    def timer(func):
        def inner(*args, **kwargs):
            match ns:
                case True:
                    time_unit = time.monotonic
                case _:
                    time_unit = time.monotonic_ns
            start_time = time_unit()
            result = func(*args, **kwargs)
            end_time = time_unit()
            print(f"Time: {end_time - start_time}")
            return result

        return inner

    return timer
