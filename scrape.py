import twitter
from time import gmtime, strftime

#Written by Dillon Merritt on April 10

api = twitter.Api(
 consumer_key='E50y90pR3tyRcJM2VrC2fA0CR',
 consumer_secret='EVGldnE7MlLlQi13OsYnL7gyIUxUj5vprnzaKyM4YKm5huEaOY',
 access_token_key='2177399604-3CnyxZqPCGlCyvzxUSsjXqseX0JFhpishSV0ioV',
 access_token_secret='jbA28AZwfCieK8CVJG1wIjWxE4djNwkOvrKTqKiAkKBiN',
 sleep_on_rate_limit=True)

results = api.GetSearch(term="#ReadyPlayerOne", raw_query=None, geocode=None, since_id=None, max_id=980694526259093504, count=100, lang="en", locale=None, result_type='recent', include_entities=False)
f= open("tweetListFinalShotForever22.txt","w+")
tweetCount = 0
id = results[0].id
print('Lowest ID is: ' + str(id))
while True:
    for result in results:

        if(id > result.id):
            id = result.id
            print('Lowest ID is: ' + str(id))
        
        f.write('[' + result.created_at + "]," + result.text.replace('\n',' ').replace(',',' '))
        f.write("\n")
        tweetCount = tweetCount + 1
    f.flush()

    results = api.GetSearch(term="#ReadyPlayerOne", raw_query=None, geocode=None, max_id=id, count=100, lang="en", locale=None, result_type='recent', include_entities=False)
    print('Grabbing more tweets...')



    
