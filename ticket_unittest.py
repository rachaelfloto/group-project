import unittest
from base import Session, engine, Base
from ticket import Ticket, query_tickets
from datetime import date


class TicketUnittest(unittest.TestCase):
    def test_ticket(self):
        # Add ticket to the database
        ticket = Ticket("Peasant", date(1975, 8, 14), "She turned me into a newt")
        Base.metadata.create_all(engine)
        session = Session()
        session.add(ticket)
        session.commit()

        # Query last ticket entered into the database
        query = session.query(Ticket).all()[-1]

        # Make sure data is equal
        self.assertEqual(query.name, "Peasant")
        self.assertEqual(query.date, date(1975, 8, 14))
        self.assertEqual(query.problem, "She turned me into a newt")

        # Remove ticket from the database
        session.delete(query)
        session.commit()

        # Ensure ticket has been removed from the database
        self.assertEqual(session.query(Ticket).get(query.id), None)
        session.close()

    def test_add(self):
        # Add ticket to the database
        ticket = Ticket("Tim the Enchanter", date(2022, 9, 24), "There are some who call me...'Tim'")
        ticket.add()

        # Query last ticket entered into the database
        Base.metadata.create_all(engine)
        session = Session()
        query = session.query(Ticket).all()[-1]

        # Make sure data is equal
        self.assertEqual(query.name, "Tim the Enchanter")
        self.assertEqual(query.date, date(2022, 9, 24))
        self.assertEqual(query.problem, "There are some who call me...'Tim'")

        # Remove ticket from the database
        session.delete(query)
        session.commit()

        # Ensure ticket has been removed from the database
        self.assertEqual(session.query(Ticket).get(query.id), None)
        session.close()

    def test_remove(self):
        # Add ticket to the database
        ticket = Ticket("Bridgekeeper", date(2077, 12, 10), "What... is the air-speed velocity of an unladen swallow?")
        ticket.add()

        # Query last ticket entered into the database
        Base.metadata.create_all(engine)
        session = Session()
        query = session.query(Ticket).all()[-1]
        session.close()

        # Make sure data is equal
        self.assertEqual(query.name, "Bridgekeeper")
        self.assertEqual(query.date, date(2077, 12, 10))
        self.assertEqual(query.problem, "What... is the air-speed velocity of an unladen swallow?")

        # Remove ticket from the database
        ticket.remove()

        # Ensure ticket has been removed from the database
        Base.metadata.create_all(engine)
        session = Session()
        self.assertEqual(session.query(Ticket).get(query.id), None)
        session.close()

    def test_query_tickets(self):
        # Add ticket to the database
        ticket = Ticket("Arthur", date(1992, 1, 19), "Please, please! No more! We shall find a shrubbery.")
        ticket.add()

        # Query last ticket entered into the database
        query = query_tickets()[-1]

        # Make sure data is equal
        self.assertEqual(query.name, "Arthur")
        self.assertEqual(query.date, date(1992, 1, 19))
        self.assertEqual(query.problem, "Please, please! No more! We shall find a shrubbery.")

        # Cleanup database
        ticket.remove()

        # Ensure ticket has been removed from the database
        Base.metadata.create_all(engine)
        session = Session()
        self.assertEqual(session.query(Ticket).get(query.id), None)
        session.close()


if __name__ == '__main__':
    unittest.main()
