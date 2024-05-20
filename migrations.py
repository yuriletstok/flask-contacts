from models import db, Contact
from faker import Factory
from app import app

app.app_context().push()

fake = Factory.create()
# Spanish
# fake = Factory.create('es_ES')
# fake = Factory.create('he_IL')
fake = Factory.create('ru_RU')
# Reload tables
db.drop_all()
db.create_all()
# Make 100 fake contacts
for num in range(100):
    fullname = fake.name().split()
    name = fullname[0]
    surname = ' '.join(fullname[1:])
    email = fake.email()
    phone = fake.phone_number()
    # Save in database
    mi_contacto = Contact(name=name, surname=surname, email=email, phone=phone)
    db.session.add(mi_contacto)

db.session.commit()
