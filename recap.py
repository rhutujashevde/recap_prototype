import os
from gpiozero import Button, LEDBoard
import time
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random

button1 = Button(14)
button2 = Button(15)
button3 = Button(18)
button4 = Button(23)
button5 = Button(24)

engine = create_engine('sqlite:///mcqaudio.sqlite')

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Mcqs(Base):
    __tablename__ = 'Mcqs'

    id = Column(Integer, primary_key = True)
    question = Column(String(250), nullable = False)
    answer = Column(String(1), nullable = False)
    result = Column(String(250), nullable = False)
    fact = Column(String(250), nullable = False)

print("welcome")
ans = "no"
while True:
    if ans == "no":
        if button1.is_pressed:
            ans = "yes"
            mcqid = random.randint(1,5)
            mcq = session.query(Mcqs).filter_by(id=mcqid).first()
            print(mcq.id)
            os.system('omxplayer '+mcq.question)
            time.sleep(0.5)
    if ans == "yes":
        if button2.is_pressed:
            ans = "a"
            time.sleep(0.5)
        elif button3.is_pressed:
            ans = "b"
            time.sleep(0.5)
        elif button4.is_pressed:
            ans = "c"
            time.sleep(0.5)
        elif button5.is_pressed:
            ans = "d"
            time.sleep(0.5)
    if ans != "yes" and ans != "no":
        print(ans)
        if ans == mcq.answer:
            print("right")
            os.system('omxplayer '+mcq.result)
            os.system('omxplayer '+mcq.fact)
            ans = "no"
        else:
            print("wrong")
            os.system('omxplayer '+mcq.result)
            os.system('omxplayer '+mcq.fact)
            ans = "no"
Base.metadata.create_all(engine)

