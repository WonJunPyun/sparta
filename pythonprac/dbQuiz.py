from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# movie = db.movies.find_one({'title':'매트릭스'},{'_id':False})
# stars = movie['star']
# print(stars)

# same_movie = list(db.movies.find({'star':stars},{'_id':False}))
#
# for same in same_movie:
#     print(same['title'])

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})


