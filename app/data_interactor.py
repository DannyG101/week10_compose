import os
from dotenv import load_dotenv
import pymysql


def get_connection():
    load_dotenv()
    try:
        return (pymysql.connect
                (user=os.getenv("DB_USER"),
                passwd=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                database=os.getenv("DB_DATABASE")))
    except Exception as err:
        raise RuntimeError(f"Failed to connect to database: {err}")

def get_all_contacts():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM contacts")
            return cursor.fetchall()

def add_contact(contact_dict:dict):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                (contact_dict["first_name"], contact_dict["last_name"], contact_dict["phone_number"])
            )
            conn.commit()
            new_id = cursor.lastrowid
            return {"message": "Contact added successfully",
                    "id":new_id}

def update_contact(user_id, contact_dict:dict):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE contacts SET first_name = %s, last_name = %s, phone_number = %s WHERE id = %s",
                           (contact_dict["first_name"], contact_dict["last_name"], contact_dict["phone_number"], user_id))
            conn.commit()
            return {"message": "Contact updated successfully"}

def delete_contact(user_id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM contacts WHERE id = %s", (user_id,))
            conn.commit()
            return {"message": "Contact deleted successfully"}


