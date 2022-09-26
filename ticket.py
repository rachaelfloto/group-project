from sqlalchemy import Column, String, Integer, Date
# TODO: Base should be from sqlalchemy.ext.declarative import declarative_base

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

