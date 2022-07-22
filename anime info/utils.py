from yuno.ui import base as uBase
from yuno.search import base as sBase
from yuno.preprocessing.filter import *
from crawler import *
import json

def get_data(index):
    json_data = json.loads(data['json'][index])
    uid = json_data['id']
    names = list(json_data["title"].values())
    img_url = json_data["coverImage"]["large"]
    
    synopsis = json_data["description"]
    anilist_url = json_data["siteUrl"]
    mal_url = "https://myanimelist.net/anime/"+str(uid)
    anime_info_dict[sBase.AnimeUid(uid)] = uBase.AnimeInfo(names,img_url,synopsis,anilist_url,mal_url)
    
def get_ani_data(index):
    json_data = json.loads(data['json'][index])
    
    uid = json_data['idMal']
    
    if not uid:
        return
    
    titles = get_anime_title(json_data)
    
    characters = []
    character_json = json_data["characters"]["edges"]
    #For each anime iterate through all characters
    for char_id in range(len(character_json)):
        
        #Get character names
        character_names = Char_Helper.get_character_names(character_json,char_id)
        if len(character_names)<1:
            continue
        
        #Fetch character gender
        gender = Char_Helper.get_character_gender(character_json,char_id)
        if gender is None:
            continue
        
        #If both characters name and gender(MALE,FEMALE) is valid, create character info then add it to anime info
        char = Character(character_names, gender)
        characters.append(char)
    
    ani_info = AnimeInfo(uid,titles,characters)
    anime_infos[sBase.AnimeUid(uid)] = ani_info