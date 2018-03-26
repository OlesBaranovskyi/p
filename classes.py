from datetime import datetime,time,date

class Subject():
    
    def __init__(self):
        self.observers = list()
       
    def attach(self,Observer ):
        self.observers.append(Observer)
       
    def detach(self,observer):
        self.observers.remove(observer)
    def Notify(self):
        for ob in self.observers:
            ob.update()
        print('Notify')

  

    

class Observer():
    def __init__(self, _subject):
        self.subject = _subject
        self.subject.attach(self)
      
    def update(self):
        print('update observer')
      

class Timer(Subject):
    def __init__(self):
        super().__init__()
        self.hour = datetime.now().hour
        self.minute = datetime.now().minute
        self.second = datetime.now().second
       
    def tick(self):
        while True:
            
            if self.second != datetime.now().second:
               self.second = datetime.now().second
               self.Notify()
        
   
class DigitalClock(Observer):
    def __init__(self,subject):
        super().__init__(subject)
        
    def update(self):
        print(self.subject.second)


  

mytimer = Timer()
mydigit = DigitalClock(mytimer)
mydigit.subject.tick()