import threading
import time
from concurrent.futures import ThreadPoolExecutor

def seconds(seconds):
    print(f"SLeeping for {seconds} seconds")
    time.sleep(seconds)
    
# # NORMAL CODE
# seconds(2)
# seconds(3)
# seconds(4)

# # Same code using threads
# def main():
    
#     t1 = threading.Thread(target=seconds,args=[2]) 
#     t2 = threading.Thread(target=seconds,args=[4]) 
#     t3 = threading.Thread(target=seconds,args=[6])

#     t1.start()
#     t2.start()
#     t3.start()

#     t1.join()
#     t2.join()
#     t3.join()

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(seconds, 3)
        future2 = executor.submit(seconds, 4)
        future3 = executor.submit(seconds, 6)

        print(future1.result())
        print(future2.result())
        print(future3.result())
        
        l = [3,5,1,2]
        results = executor.map(seconds,l)
        for result in results:
            print(result)
            

poolingDemo()

# main()


