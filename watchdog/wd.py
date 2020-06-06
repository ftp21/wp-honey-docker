import sys
import time
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("wd.log",'w'),
 #       logging.StreamHandler()
    ]
)
def run(folder="test"):
    path = folder
    os.chdir(path)
    logging.info(f"Monitored directory {path}")
    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        exit(1)
    observer.join()

#with daemon.DaemonContext(
#        pidfile="wd.pid",
#        ) as context:

if __name__ == "__main__":
    run(sys.argv[1])
