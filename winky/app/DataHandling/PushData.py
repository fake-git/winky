
# import os
# import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'winky.settings')
# django.setup()
#
#
# firstNames = []
# lastNames = []
#
# first = open('/home/berlin/Desktop/us.txt', 'r')
# last = open('/home/berlin/Desktop/all.txt', 'r')
#
#
# fn = first.readlines()
# ln = last.readlines()
#
#
# i = 0
# k = 0
#
#
# for line1 in fn:
#     if i > 999:
#         break
#
#     line1 = line1.replace('\n', '')
#     firstNames.append(line1)
#     i += 1
#
#
# for line2 in ln:
#     if k > 999:
#         break
#
#     line2 = line2.replace('\n', '')
#     lastNames.append(line2)
#     k += 1
#
#
# ###################################################################
#
# from app.models import User
#
#
# for index in range(1000):
#     fname = firstNames[index]
#     lname = lastNames[index]
#     mail = f'{fname}_{lname}@gmail.com'
#     password = '12345678'
#
#     print(i)
#
#     new_user = User(first_name=fname, last_name=lname, email=mail, password=password)
#     new_user.save()
#
#






