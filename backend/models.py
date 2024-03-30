from config import db

# This class is a model for the Contact table in the database

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)

    def to_json(self):
        
        # Used CamelCase for the keys and snake_case for the values

        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "phone": self.phone
        }