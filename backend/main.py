from flask import request, jsonify
from config import app, db
from models import Contact

# CRUD Backend

@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json["firstName"]
    last_name = request.json["lastName"]
    phone = request.json["phone"]

    if not first_name or not last_name or not phone:
        return jsonify({"message": "Missing data. Please try again."}), 400

    contact = Contact(first_name=first_name, last_name=last_name, phone=phone)
    try:
        db.session.add(contact)
        db.session.commit()
        return jsonify({"message": "Contact created!"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@app.route("/update_contact/<int:id>", methods=["PUT"])
def update_contact(id):
    contact = Contact.query.get(id)

    if not contact:
        return jsonify({"message": "Contact not found."}), 404

    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.phone = data.get("phone", contact.phone)

    db.session.commit()

    return jsonify({"message": "Contact updated!"})

@app.route("/delete_contact/<int:id>", methods=["DELETE"])
def delete_contact(id):
    contact = Contact.query.get(id)

    if not contact:
        return jsonify({"message": "Contact not found."}), 404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "Contact deleted!"})



if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Create all the models in the database

    app.run(debug=True)

