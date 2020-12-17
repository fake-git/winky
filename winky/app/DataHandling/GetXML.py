# import xmltodict
# import urllib.request
# import os
# import django
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'winky.settings')
# django.setup()
#
# from app.models import Movies
#
#
#
#
#
# url = 'https://rss.itunes.apple.com/api/v1/us/movies/top-movies/action-and-adventure/25/explicit.rss'
#
# with urllib.request.urlopen(url) as response:
#     response_dict = xmltodict.parse(response)
#     print(response_dict)
#     bbb = response_dict['rss']['channel']['item'][0]
#
#     for i in range(25):
#
#         title = response_dict['rss']['channel']['item'][i]['description']
#         actor = response_dict['rss']['channel']['item'][i]['category'][0]['#text']
#         rate = 0.0
#         img = response_dict['rss']['channel']['item'][i]['link']
#
#
#         print(f'{title}  {actor}  {rate}  {img}')
#         new_movie = Movies(title=title, actor=actor, rate=rate, img=img)
#         new_movie.save()
#
#

