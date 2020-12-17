# import os
# import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'winky.settings')
# django.setup()
#
# from app.models import Movies
# import time
# from selenium import webdriver
#
#
#
# driver_path = '/home/berlin/PycharmProjects/winky/app/Driver/chromedriver'
# driver = webdriver.Chrome(executable_path=driver_path)
#
#
# all_movies = Movies.objects.all()
#
#
# for movie in all_movies:
#
#     if int(movie.id) > :
#
#         time.sleep(1)
#         driver.get(movie.img)
#         time.sleep(4)
#
#         img_path = f'../images/{movie.id}.png'
#
#         # with open(img_path, 'wb') as file:
#         #     file.write(driver.find_element_by_xpath('/html/body/div[4]/div/main/div/div/div/div[3]/section[1]/div[2]/div[1]/picture/img').screenshot_as_png)
#
#         rate = driver.find_element_by_xpath('/html/body/div[4]/div/main/div/div/div/div[3]/section[1]/div[2]/div[2]/div[1]/div[2]/header/ul[2]/li[2]/ul/li/figure/figcaption')
#         rate = rate.get_attribute('innerHTML')
#         rate = rate.split('•')
#         rate = rate[0].replace(' ', '')
#
#         converted_rate = float(rate)
#         print(converted_rate)
#
#         movie.img = img_path
#         movie.rate = converted_rate
#         movie.save()
#         time.sleep(1)
#

