from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
class EventHandler(FileSystemEventHandler):
   def __init__(self,queue):
       super(FileSystemEventHandler, self).__init__()
       self.queue=queue
   def on_any_event(self, event):
        myevent={}
        myevent['is_dir']=False
        myevent['event']=event.event_type
        try:
            myevent['src']=event.src_path
            myevent['dest']=event.dest_path
            if event.is_directory==True:
                myevent['is_dir']=True
            else:
                myevent['is_dir']=False
        except AttributeError:
            myevent['src']=event.src_path
            myevent['dest']=False
            if event.is_directory==True:
                myevent['is_dir']=True
            else:
                myevent['is_dir']=False
        self.queue.put(myevent)

class Watcher():
    def __init__(self,monpath,queue):
        self.event_handler = EventHandler(queue)
        self.observer = Observer()
        self.monpath=monpath
        self.queue=queue
    def start(self):
        self.observer.schedule(self.event_handler, self.monpath, recursive=True)
        self.observer.start()
    def stop(self):
        self.observer.stop()
    def join(self):
        self.observer.join()
