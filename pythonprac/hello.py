# # fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
# #
# # count = 0
# # for fruit in fruits:
# #     if ff == '수박' :
# #         count += 1
# #
# # print(count)
# #
# # people = [{'name': 'bob', 'age': 20},
# #           {'name': 'carry', 'age': 38},
# #           {'name': 'john', 'age': 7},
# #           {'name': 'smith', 'age': 17},
# #           {'name': 'ben', 'age': 27}]
# #
# # for person in people:
# #     if person['age'] < 20 :
# #         print(person['name'],person['age'])
#
# import requests # requests 라이브러리 설치 필요
#
# r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
# rjson = r.json()
#
# # print(rjson['RealtimeCityAir']['row'][0]['MSRSTE_NM'])
#
# gus = rjson['RealtimeCityAir']['row']
#
# for gu in gus :
#     gu_name = gu['MSRSTE_NM']
#     gu_mise = gu['IDEX_MVL']
#     if gu_mise > 100 :
#         print(gu_name, gu_mise)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')

# print(title['href'])

#old_content > table > tbody > tr:nth-child(2) >

trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    a_tag = tr.select_one(' td.title > div > a')
    if a_tag is not None:
        title = a_tag.text
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        star = tr.select_one('td.point').text
        doc = {
            'rank':rank,
            'title':title,
            'star':star
        }
        db.movies.insert_one(doc)

#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(2) > td.point



