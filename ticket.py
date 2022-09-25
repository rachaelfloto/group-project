from sqlalchemy import Column, String, Integer, Date
from base import Session, engine, Base


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


# Add a new ticket to the SQL database
def add_ticket(name, date, problem):
    Base.metadata.create_all(engine)
    session = Session()
    ticket = Ticket(name, date, problem)
    session.add(ticket)
    session.commit()
    session.close()


# Query all tickets from the SQL database
def query_tickets():
    Base.metadata.create_all(engine)
    session = Session()
    tickets = session.query(Ticket).all()
    session.close()
    return tickets
