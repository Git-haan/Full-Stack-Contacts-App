import { useState } from "react"

const ContactForm = ({ existingContact = {}, updateCallback }) => {
    const [firstName, setFirstName] = useState(existingContact.firstName || "")
    const [lastName, setLastName] = useState(existingContact.lastName ||"")
    const [phone, setPhone] = useState(existingContact.phone ||"")

    const updating = Object.entries(existingContact).length !== 0

    const handleSubmit = async (e) => {
        e.preventDefault()

        const data = {
            firstName,
            lastName,
            phone
        }

        const url = "http://127.0.0.1:5000/" + (updating ? `update_contact/${existingContact.id}` : "create_contact")
        const options = {
            method: updating ? "PUT" : "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
        const response = await fetch(url, options)

        if (response.status != 201 && response.status != 200) {
            const data = await response.json()
            alert(data.message)
        } else {
            updateCallback()
        }
    }

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="firstName">First Name</label>
                <input 
                    type = "text" 
                    placeholder = "Enter First Name" 
                    id="firstName" 
                    value = {firstName} 
                    onChange = {(e) => setFirstName(e.target.value)} 
                />
            </div>
            <div>
                <label htmlFor="lastName">Last Name</label>
                <input 
                    type = "text" 
                    placeholder = "Enter Last Name" 
                    id="lastName" 
                    value = {lastName} 
                    onChange = {(e) => setLastName(e.target.value)} 
                />
            </div>
            <div>
                <label htmlFor="phone">Phone Number</label>
                <input 
                    type = "text" 
                    placeholder = "Enter Phone Number" 
                    id="phone" 
                    value = {phone} 
                    onChange = {(e) => setPhone(e.target.value)} 
                />
            </div>
            <button type = "submit">{updating ? "Update" : "Create"}</button>
        </form>
    )
}

export default ContactForm