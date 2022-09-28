from sqlalchemy import Column, String, Integer, Date
from database import Base
from database import engine
from database import newSession


# Create and map the ticket class
class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(Date)
    problem = Column(String)

    def __init__(self, name, date, problem):
        self.name = name
        self.date = date
        self.problem = problem

    # Add ticket to SQL database
    def add(self):
        Base.metadata.create_all(engine)
        session = newSession()
        session.add(self)
        session.commit()
        session.close()

    # Remove ticket from SQL database
    def remove(self):
        Base.metadata.create_all(engine)
        session = newSession()
        session.delete(self)
        session.commit()
        session.close()


# Query all tickets from the SQL database
def query_tickets():
    Base.metadata.create_all(engine)
    session = newSession()
    tickets = session.query(Ticket).all()
    session.close()
    return tickets
