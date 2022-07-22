# AniSuggest

## Review-based anime recommender

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

AniSuggest is a simple review-based anime recommender.

- Insert a short description of anime content you would like(E.g. "Anime with good music")
- Get anime recommendations
- ✨Simple✨

## Features

- Use reviews as a main source of information for recommendation.
- Extract relevant information from the user’s textual reviews.
- Reviews are preprocessed based on Yuno(incl. formatting, summarizing, replace names with token)
- Use cosine similarity score as metric.

Review is a source of useful information to find anime or any movie that suit you, 
in most case you would like ask your friends but you don't want to disturb them.
Then, AniSuggest can suggest some anime based to your preferences.

## Tech

AniSuggest uses a number of open source projects to work properly:

- [MAL API] - MyAnimeList's API that we crawled reviews and anime data with.
- [Anilist crawler] - Anilist crawler for character data such as names and gender.
- [Yuno] - Provide the base for preprocessing.
- [Python] - The program is written in Python 3.9.


And of course AniSuggest itself is open source.

## Installation

AniSuggest requires [Python] to run.

The repository has only been tested with Python v3.9 on Windows.

Clone this repository
```
git clone https://github.com/Alkahestry/AniSuggest.git
```
Clone [Yuno] and put it in AniSuggest folder (same level as /crawler). Only preprocessing, ui, search folders are necessary.

```
git clone https://github.com/IAmPara0x/Yuno.git
```

You may have to download extra dependencies if necessary. We use pip for that.
## Usage

- Crawl anime data using anilist crawler.
- Get anime info with anilist data file 
```
python get_anime_info.py --path [path of anilist data file]
```
- Alter the path for anime_info and reviews in reviews.ipynb to process the reviews.
- Change the input and necessary paths in recommender.py to get recommendation.


## License

MIT


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
    
   [Anilist Crawler]: <https://github.com/soruly/anilist-crawler>
   [MAL API]: <https://myanimelist.net/apiconfig/references/api/v2>
   [Yuno]: <https://github.com/IAmPara0x/Yuno>
   [Python]: <https://www.python.org/>
   
   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
