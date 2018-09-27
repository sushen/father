from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data_map import Base, UserInfo, UserAddress

engine = create_engine('sqlite:///father.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Add Lots of user

#User No -2
UserInfo_2 = UserInfo(email="UrbanBurger2@gmail.com")

session.add(UserInfo_2)
session.commit()

UserAddress_2 = UserAddress(firstname ="VeggieBurger", lastname="Juicy",phone="01725588361", userinfo=UserInfo_2)

session.add(UserAddress_2)
session.commit()

#User No -3
UserInfo_3 = UserInfo(email="UrbanBurger3@gmail.com")

session.add(UserInfo_3)
session.commit()

UserAddress_3 = UserAddress(firstname ="VeggieBurger3", lastname="Juicy3",phone="01725588363", userinfo=UserInfo_3)

session.add(UserAddress_3)
session.commit()

#User No -4
UserInfo_4 = UserInfo(email="UrbanBurger4@gmail.com")

session.add(UserInfo_4)
session.commit()

UserAddress_4 = UserAddress(firstname ="VeggieBurger4", lastname="Juicy4",phone="01725588364", userinfo=UserInfo_4)

session.add(UserAddress_4)
session.commit()

#User No -5
UserInfo_5 = UserInfo(email="UrbanBurger5@gmail.com")

session.add(UserInfo_5)
session.commit()

UserAddress_5 = UserAddress(firstname ="VeggieBurger5", lastname="Juicy5",phone="01725588365", userinfo=UserInfo_5)

session.add(UserAddress_5)
session.commit()


print ("added menu items!")