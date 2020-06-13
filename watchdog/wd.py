import sys
import time
import logging
import queue
from inc.watcher import EventHandler,Watcher

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("wd.log",'w'),
        logging.StreamHandler()
    ]
)
def run(folder="."):
    logging.info(f"Monitored directory {folder}")
    q=queue.Queue()
    watch=Watcher(folder,q)
    watch.start()
    try:
       while True:
            logging.info(q.get())
            time.sleep(1)
    except KeyboardInterrupt:
       watch.stop()
       exit(1)
    watch.join()


if __name__ == "__main__":
     run(sys.argv[1])
