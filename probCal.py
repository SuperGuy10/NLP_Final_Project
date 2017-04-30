from takeFeature import sorted_JJ, sorted_RB,sorted_NN,sorted_VB,\
                        sorted_HP_JJ,sorted_HP_RB,sorted_HP_NN,sorted_HP_VB,\
                        sorted_SD_JJ,sorted_SD_RB,sorted_SD_NN,sorted_SD_VB,\
                        artists_dict,HP_artists_dict,SD_artists_dict,\
                        genres_dict,HP_genres_dict,SD_genres_dict 
                   
TOP5_JJ = sorted_JJ[-5:]
TOP5_RB = sorted_RB[-6:-1]
TOP5_NN = sorted_NN[-5:]
TOP5_VB = sorted_VB[-5:]

prob_HP_JJ = {}
prob_HP_RB = {}
prob_HP_NN = {}
prob_HP_VB = {}

#calculate happy adjective probability
for x in range(len(TOP5_JJ)):
    for y in range(len(sorted_HP_JJ)):
        if (TOP5_JJ[x][0] == sorted_HP_JJ[y][0]):
            if (TOP5_JJ[x][0]) not in prob_HP_JJ:
                prob_HP_JJ[TOP5_JJ[x][0]] = (sorted_HP_JJ[y][1]) / (TOP5_JJ[x][1]) 

#calculate happy adverb probability               
for x in range(len(TOP5_RB)):
    for y in range(len(sorted_HP_RB)):
        if (TOP5_RB[x][0] == sorted_HP_RB[y][0]):
            if (TOP5_RB[x][0]) not in prob_HP_RB:
                prob_HP_RB[TOP5_RB[x][0]] = (sorted_HP_RB[y][1]) / (TOP5_RB[x][1])

#calculate happy noun probability
for x in range(len(TOP5_NN)):
    for y in range(len(sorted_HP_NN)):
        if (TOP5_NN[x][0] == sorted_HP_NN[y][0]):
            if (TOP5_NN[x][0]) not in prob_HP_NN:
                prob_HP_NN[TOP5_NN[x][0]] = (sorted_HP_NN[y][1]) / (TOP5_NN[x][1])                

#calculate happy verb probability
for x in range(len(TOP5_VB)):
    for y in range(len(sorted_HP_VB)):
        if (TOP5_VB[x][0] == sorted_HP_VB[y][0]):
            if (TOP5_VB[x][0]) not in prob_HP_VB:
                prob_HP_VB[TOP5_VB[x][0]] = (sorted_HP_VB[y][1]) / (TOP5_VB[x][1])
    
prob_SD_JJ = {}
prob_SD_RB = {}
prob_SD_NN = {}
prob_SD_VB = {}

#calculate sad adjective probability
for x in range(len(TOP5_JJ)):
    for y in range(len(sorted_SD_JJ)):
        if (TOP5_JJ[x][0] == sorted_SD_JJ[y][0]):
            if (TOP5_JJ[x][0]) not in prob_SD_JJ:
                prob_SD_JJ[TOP5_JJ[x][0]] = (sorted_SD_JJ[y][1]) / (TOP5_JJ[x][1]) 

#calculate sad adverb probability                
for x in range(len(TOP5_RB)):
    for y in range(len(sorted_SD_RB)):
        if (TOP5_RB[x][0] == sorted_SD_RB[y][0]):
            if (TOP5_RB[x][0]) not in prob_SD_RB:
                prob_SD_RB[TOP5_RB[x][0]] = (sorted_SD_RB[y][1]) / (TOP5_RB[x][1])

#calculate sad noun probability                
for x in range(len(TOP5_NN)):
    for y in range(len(sorted_SD_NN)):
        if (TOP5_NN[x][0] == sorted_SD_NN[y][0]):
            if (TOP5_NN[x][0]) not in prob_SD_NN:
                prob_SD_NN[TOP5_NN[x][0]] = (sorted_SD_NN[y][1]) / (TOP5_NN[x][1])                

#calculate sad verb probability                
for x in range(len(TOP5_VB)):
    for y in range(len(sorted_SD_VB)):
        if (TOP5_VB[x][0] == sorted_SD_VB[y][0]):
            if (TOP5_VB[x][0]) not in prob_SD_VB:
                prob_SD_VB[TOP5_VB[x][0]] = (sorted_SD_VB[y][1]) / (TOP5_VB[x][1])


prob_HP_artists = {}
prob_HP_genres = {}

prob_SD_artists = {}
prob_SD_genres = {}

for key_artist in HP_artists_dict:
    prob_HP_artists[key_artist] = HP_artists_dict[key_artist] / artists_dict[key_artist]
#print (prob_HP_artists)

for key_artist in SD_artists_dict:
    prob_SD_artists[key_artist] = SD_artists_dict[key_artist] / artists_dict[key_artist]
#print (prob_SD_artists) 
    
for key_genre in HP_genres_dict:
    prob_HP_genres[key_genre] = HP_genres_dict[key_genre] / genres_dict[key_genre]
#print (prob_HP_genres)

for key_genre in SD_genres_dict:
    prob_SD_genres[key_genre] = SD_genres_dict[key_genre] / genres_dict[key_genre]
#print (prob_SD_genres)   
    
