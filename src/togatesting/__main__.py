""" import queue
import threading,time,random """

from togatesting.app import main

""" def func(id, result_queue):
    print("Thread", id)
    time.sleep(random.random() * 5)
    result_queue.put((id, 'done'))

def main():
    q = queue.Queue()
    threads = [ threading.Thread(target=func, args=(i, q)) for i in range(5) ]
    for th in threads:
        th.daemon = True
        th.start()

    result1 = q.get()
    result2 = q.get()
    
    print("First result: {}".format(result1))
    print("Second result: {}".format(result2))

    return main """

if __name__ == "__main__":
    main().main_loop()
