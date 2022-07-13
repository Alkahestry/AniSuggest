from sqlalchemy import true
from yuno.preprocessing.filter import Gender
gender_dict = {}
gender_dict['MALE'] = Gender.MALE
gender_dict['FEMALE'] = Gender.FEMALE

class Char_Helper:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def get_character_names(json_data,char_id) -> list:
        
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
        
        def isName(name : str) -> bool:
            """
            True if name of Character is not None and lenght is more than 1
            """
            return name is not None and len(name) > 1

        char_name = extract_name(json_data,char_id)
        first_name, last_name = get_first_and_last_name(char_name)
        
        name_lst = [alt for alt in char_name['alternative']]
        
        if isName(first_name):
            name_lst.append(first_name)
            
        return name_lst
    
    @staticmethod
    def get_character_gender(json_data,character_id):
        
        def get_gender(json_data,character_id):
            gender = json_data[character_id]['node']['gender']
            return gender

        def isValidGender(gender : str) -> bool:
            return gender in ['Male','Female']
        
        try:
            char_gender = get_gender(json_data,character_id)
        except:
            char_gender = None
        
        if not isValidGender(char_gender):
            return
        else:
            gender = gender_dict[str(char_gender).upper()]
            
        return gender
        
    
    