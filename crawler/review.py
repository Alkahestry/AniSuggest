from yuno1.preprocessing.summarizer import *
from yuno1.preprocessing.filter import *
from yuno1.preprocessing.sentencizer import *

# rs = ReviewSentencizer(nlp=spacy.load("en_core_web_sm"))
# summer = Summarizer()
# filt = FilterText(list(anime_info.values()))

class Review:
    def __init__(self, nlp = spacy.load("en_core_web_sm"), *args, **kwargs):
        self.nlp = nlp
        self.sentencizer = ReviewSentencizer(nlp=nlp)
        self.summarizer = Summarizer()
        self.filter = FilterText(list(kwargs['anime_info'].values()))
        self.reviews = kwargs['reviews']
        
    def __str__(self):
        pass
    
    def format_txt(self, index : int) -> str:
        return self.sentencizer.format_text(self.reviews['text'][index])
    
    def sentencizer_func(self, str : str) -> list:
        print("Sentencizer", type(str))
        return self.sentencizer.sents(str)
    
    def summarizer_func(self, str) -> list:
        return self.summarizer.summarize(str)
    
    def filter_text(self, index : int, str : list) -> list:
        print(f"Filter {type(str)}")
        return self.filter.filter_all(self.reviews['anime_uid'][index], str)
    
    def process(self, index : int):
        str = self.format_txt(index)
        print(f"Return format_txt {type(str)}")
        str = self.sentencizer_func(str)
        print(f"Return sentencizer {type(str)}")
        str = self.summarizer_func(str)
        print(f"Return summarizer {type(str)}")
        str = self.filter_text(index, str)
        print(f"Return filter_text {type(str)}")
#         Return format_txt <class 'str'>
# Sentencizer <class 'str'>
# Return sentencizer <class 'list'>
# Return summarizer <class 'list'>
# Filter <class 'list'>
# Return filter_text <class 'list'>
        # str = self.sentencizer.format_text(self.reviews['text'][index])
        # str = self.sentencizer.sents(str)
        # str = self.summarizer.summarize(str)
        # str = self.filter.filter_all(self.reviews['anime_uid'][index],str)
        
        def list_of_list_to_list(l):
            return [item for sublist in l for item in sublist]
        
        if type(str[0]) == list:
            str = list_of_list_to_list(str)
            
        return str
        