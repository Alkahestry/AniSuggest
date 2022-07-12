class Character:
    def __init__(self) -> None:
        pass

    def extract_name(json_data, character_id):
        """
        Extracts the name of the character from JSON data
        """
        name = json_data[character_id]['node']['name']
        return name
    
    def get_first_and_last_name(name):
        """
        Extracts the first and last name of the character from its name
        """
        first_name = name['first']
        last_name = name['last']
        return first_name, last_name

