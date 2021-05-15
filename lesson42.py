import time

def decor(f):
    def f_wrapper():
        time1 = time.time()
        f()
        time2 = time.time()
        print(f"Passed {time2-time1} seconds.")

    return f_wrapper


@decor
def hi():
    time.sleep(1)


hi()
