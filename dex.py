import sqlite3

def connect_to_db(db_name):
    """Connect to SQLite database (creates file if it doesn't exist)"""
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    """Create a table if it doesn't exist"""
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        type1 TEXT NOT NULL,
        type2 TEXT,
        hp INTEGER,
        attack INTEGER,
        defense INTEGER,
        speed INTEGER,
        special_attack INTEGER,
        special_defense INTEGER,
        abilities TEXT
    )
    """)
    conn.commit()

def add_pokemon(conn, id, name, type1, type2, hp, attack, defense, speed, special_attack, special_defense, abilities):
    """Add a new Pokemon to the database"""
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO pokemon (id, name, type1, type2, hp, attack, defense, speed, special_attack, special_defense, abilities)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (id, name, type1, type2, hp, attack, defense, speed, special_attack, special_defense, abilities))
    conn.commit()

def search_pokemon_by_id(conn, id):
    """Search for a Pokemon by ID"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pokemon WHERE id=?", (id,))
    results = cursor.fetchall()
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Type1: {row[2]}, Type2: {row[3]}, HP: {row[4]}, Attack: {row[5]}, Defense: {row[6]}, Speed: {row[7]}, Special Attack: {row[8]}, Special Defense: {row[9]}, Abilities: {row[10]}")

def search_pokemon_by_name(conn, name):
    """Search for a Pokemon by name"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pokemon WHERE name=?", (name,))
    results = cursor.fetchall()
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Type1: {row[2]}, Type2: {row[3]}, HP: {row[4]}, Attack: {row[5]}, Defense: {row[6]}, Speed: {row[7]}, Special Attack: {row[8]}, Special Defense: {row[9]}, Abilities: {row[10]}")

def search_pokemon_by_type(conn, type):
    """Search for a Pokemon by type"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pokemon WHERE type1=? OR type2=?", (type, type))
    results = cursor.fetchall()
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Type1: {row[2]}, Type2: {row[3]}, HP: {row[4]}, Attack: {row[5]}, Defense: {row[6]}, Speed: {row[7]}, Special Attack: {row[8]}, Special Defense: {row[9]}, Abilities: {row[10]}")

def delete_pokemon(conn, id):
    """Delete a Pokemon by ID"""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pokemon WHERE id=?", (id,))
    conn.commit()

def edit_pokemon(conn, id, name, type1, type2, hp, attack, defense, speed, special_attack, special_defense, abilities):
    """Edit a Pokemon by ID"""
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE pokemon
    SET name=?, type1=?, type2=?, hp=?, attack=?, defense=?, speed=?, special_attack=?, special_defense=?, abilities=?
    WHERE id=?
    """, (name, type1, type2, hp, attack, defense, speed, special_attack, special_defense, abilities, id))
    conn.commit()

def display_all_pokemon(conn):
    """Display all Pokemon"""
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, type1, type2, hp, attack, defense, speed, special_attack, special_defense, abilities FROM pokemon")
    results = cursor.fetchall()
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Type1: {row[2]}, Type2: {row[3]}, HP: {row[4]}, Attack: {row[5]}, Defense: {row[6]}, Speed: {row[7]}, Special Attack: {row[8]}, Special Defense: {row[9]}, Abilities: {row[10]}")

def main():
    conn = connect_to_db("pokedex.db")
    create_table(conn)
    
    while True:
        print("-----POKEDEX-----")
        print("1. Data Entry Mode")
        print("2. Search Mode")
        print("3. Edit Mode")
        print("4. Delete Mode")
        print("5. Display All Pokemon")
        print("6. Exit")
        option = int(input("Enter your option: ").strip())
        
        if option == 1:
            while True:
                id = int(input("Enter Pokemon ID: "))
                name = input("Enter Pokemon Name: ")
                type1 = input("Enter Primary type: ")
                type2 = input("Enter Secondary type (or 'None'): ")
                hp = int(input("Enter HP: "))
                attack = int(input("Enter Attack: "))
                defense = int(input("Enter Defense: "))
                speed = int(input("Enter Speed: "))
                special_attack = int(input("Enter Special Attack: "))
                special_defense = int(input("Enter Special Defense: "))
                abilities = input("Enter Abilities: ")
                add_pokemon(conn, id, name, type1, type2, hp, attack, defense, speed, special_attack, special_defense, abilities)
                cont = input("Do you want to add more Pokemon? (y/n): ").strip().lower()
                if cont != 'y':
                    break
        elif option == 2:
            while True:
                print("\n--- Search Mode ---")
                print("1. Search by ID")
                print("2. Search by Name")
                print("3. Search by Type")
                print("4. Exit Search Mode")
                choice = int(input("Enter your choice: ").strip())
                
                if choice == 1:
                    id = int(input("Enter Pokemon ID to search: "))
                    search_pokemon_by_id(conn, id)
                elif choice == 2:
                    name = input("Enter Pokemon Name to search: ")
                    search_pokemon_by_name(conn, name)
                elif choice == 3:
                    type = input("Enter Pokemon Type to search: ")
                    search_pokemon_by_type(conn, type)
                elif choice == 4:
                    break
                else:
                    print("Invalid choice! Please try again.")
        elif option == 3:
            id = int(input("Enter Pokemon ID to edit: "))
            name = input("Enter new Name: ")
            type1 = input("Enter new Primary Type: ")
            type2 = input("Enter new Secondary Type (or 'None'): ")
            hp = int(input("Enter new HP: "))
            attack = int(input("Enter new Attack: "))
            defense = int(input("Enter new Defense: "))
            speed = int(input("Enter new Speed: "))
            special_attack = int(input("Enter new Special Attack: "))
            special_defense = int(input("Enter new Special Defense: "))
            abilities = input("Enter new Abilities: ")
            edit_pokemon(conn, id, name, type1, type2, hp, attack, defense, speed, special_attack, special_defense, abilities)
        elif option == 4:
            id = int(input("Enter Pokemon ID to delete: "))
            delete_pokemon(conn, id)
        elif option == 5:
            display_all_pokemon(conn)
        elif option == 6:
            print("Exiting.....")
            break
        else:
            print("Invalid Option! Select correct option....")
    
    conn.close()

if __name__ == "__main__":
    main()