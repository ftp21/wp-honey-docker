from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
class EventHandler(FileSystemEventHandler):
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
	return myevent

class Watcher():
    def __init__(self,monpath):
        event_handler = EventHandler()
        observer = Observer()
	self.monpath=monpath
    def start(self):
	self.observer.schedule(event_handler, self.monpath, recursive=True)
        self.observer.start()
    def stop(self):
        self.observer.stop()
    def join(self):
        self.observer.join()
