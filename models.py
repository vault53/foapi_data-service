from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Consumable(Base):
    __tablename__ = 'consumables'

    id = Column(Integer, primary_key=True)
    type = Column('type', String)
    subtype = Column('subtype', String)
    name = Column('name', String, unique=True)
    image = Column('image', String, unique=True)
    addiction_rate = Column('addiction_rate', String)
    weight = Column('weight', Integer)
    value = Column('value', Integer)
    effects = Column('effects', String)

    def __repr__(self):
        return "<consumable(name='%s')>" % self.name


engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()
consumable = Consumable()
consumable.id = 0
consumable.type = 'item'
consumable.subtype = 'consumable'
consumable.image = 'https://vignette.wikia.nocookie.net/fallout/images/7/76/Chem_Antidote.png/revision/latest?cb=20170916191532'
consumable.name = 'antidote'
consumable.addiction_rate = '0'
consumable.weight = 1
consumable.value = 50
consumable.effects = '{ "when": "Immediate", "type": "poison", "value": "-25" }, ' \
                     '{ "when": "after 1 minute", "type": "poison", "value": "-25" }, ' \
                     '{ "when": "after 2 minutes", "type": "poison", "value": "-25" }, '

session.add(consumable)
session.commit()

consumables = session.query(Consumable).all()
for con in consumables:
    print(f'{con.id}\n'
          f'{con.name}\n'
          f'{con.addiction_rate}\n'
          f'{con.weight}\n'
          f'{con.value}\n'
          f'{con.effects}\n'
          f'{con.type}\n'
          f'{con.subtype}\n'
          f'{con.image}\n')

session.close()
