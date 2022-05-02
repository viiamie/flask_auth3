import logging

from app import db
from app.db.models import User, Location
from faker import Faker

def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Location).count() == 0
        #showing how to add a record
        #create a record
        user = User('keith@webizly.com', 'testtest')
        #add it to get ready to be committed
        db.session.add(user)
        #call the commit
        #db.session.commit()
        #assert that we now have a new user
        #assert db.session.query(User).count() == 1
        #finding one user record by email
        user = User.query.filter_by(email='keith@webizly.com').first()
        log.info(user)
        #asserting that the user retrieved is correct
        assert user.email == 'keith@webizly.com'
        #this is how you get a related record ready for insert
        user.locations= [Location("test","map","200","1000"),Location("test2","mp","300","2000")]
        #commit is what saves the songs
        db.session.commit()
        assert db.session.query(Location).count() == 2
        location1 = Location.query.filter_by(title='test').first()
        assert location1.title == "test"
        #changing the title of the song
        location1.title = "SuperLocationTitle"
        #saving the new title of the song
        db.session.commit()
        location2 = Location.query.filter_by(title='SuperLocationTitle').first()
        assert location2.title == "SuperLocationTitle"
        #checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Location).count() == 0




