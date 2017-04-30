import os
import nltk
from nltk.tokenize import word_tokenize as wt
from probCal import prob_HP_JJ,prob_HP_RB, prob_HP_NN, prob_HP_VB,\
                    prob_SD_JJ,prob_SD_RB, prob_SD_NN, prob_SD_VB,\
                    prob_HP_artists, prob_HP_genres,prob_SD_artists,prob_SD_genres,\
                    artists_dict,genres_dict


def lyricsClassify (artist, genre, lyric_address, lyric_name):
    
    artistHPPro = 1
    artistSDPro = 1
    genreHPPro = 1
    genreSDPro = 1
    
    #calculate artist probability
    if artist in prob_HP_artists:
        artistHPPro = prob_HP_artists[artist]
    else:
        artistHPPro = 0.1
    
    if artist in prob_SD_artists:
        artistSDPro = prob_SD_artists[artist]
    else:
        artistSDPro = 0.1
    
    #calculate genre probability
    
    if genre in prob_HP_genres:
        genreHPPro = prob_HP_genres[genre]
    else:
        genreHPPro = 0.1
        
    if genre in prob_SD_genres:
        genreSDPro = prob_SD_genres[genre]
    else:
        genreSDPro = 0.1
    
    ly_JJ = []
    ly_RB = []
    ly_NN = []
    ly_VB = []
    happyPrb = 1
    sadPrb = 1
    rlyrics = open(os.path.join(lyric_address, lyric_name))
    wt_ly = wt(rlyrics.read())
    pt_ly = nltk.pos_tag(wt_ly)
    len_ptly = len(pt_ly)
    
    for n in range(len_ptly):
        if pt_ly[n][1] in ["JJ", "JJR", "JJS"] :
            if pt_ly[n][0] not in ly_JJ:
                ly_JJ.append(pt_ly[n][0])
        
        elif pt_ly[n][1] in ["RB", "RBR", "RBS"] :
            if pt_ly[n][0] not in ly_RB:
                ly_RB.append(pt_ly[n][0])
        
        elif pt_ly[n][1] in ["NN", "NNS", "NNP", "NNPS"] :
            if pt_ly[n][0] not in ly_NN:
                ly_NN.append(pt_ly[n][0])
        
        elif pt_ly[n][1] in ["VB", "VBD", "VBZ", "VBN", "VBP", "VBG"]:
            if pt_ly[n][0] not in ly_VB:
                ly_VB.append(pt_ly[n][0])
    
    for word in ly_JJ:
        #word in happy
        if word in prob_HP_JJ:
            happyPrb = happyPrb * prob_HP_JJ[word]
            #print ("hpjj", happyPrb)
        if word in prob_SD_JJ:
            sadPrb = sadPrb * prob_SD_JJ[word]
            #print (sadPrb)
    
    for word in ly_RB:    
        if word in prob_HP_RB:
            happyPrb = happyPrb * prob_HP_RB[word]
            #print ("hprb",happyPrb)
        if word in prob_SD_RB:
            sadPrb = sadPrb * prob_SD_RB[word]
            #print (sadPrb)
    
    for word in ly_NN:
        if word in prob_HP_NN:
            happyPrb = happyPrb * prob_HP_NN[word]
           # print ("hpnn", happyPrb)
        if word in prob_SD_NN:
            sadPrb = sadPrb * prob_SD_NN[word]
            #print (sadPrb)
    
    for word in ly_VB:
        if word in prob_HP_VB:
            happyPrb = happyPrb * prob_HP_VB[word]
            #print ("hpvb",happyPrb)
        if word in prob_SD_VB:
            sadPrb = sadPrb * prob_SD_VB[word]    
            #print (sadPrb)
    
    happyPrb = artistHPPro * genreHPPro * happyPrb
    sadPrb = artistSDPro * genreSDPro * sadPrb
    print ("The probability for this one belong to happy emotion is:", happyPrb)
    print("The probability for this one belong to sad emotion is:", sadPrb)
    
    if (happyPrb > sadPrb):
        print ("The emotion of this song is happy")
    else:
        print ("The emotion of this song is sad")

artist = input("Please type the artist:")
genre = input("Please type the gener:")
lyric_address = input("Please type the lyric's address:")
lyric_name = input("Please type the lyric name:")

run = lyricsClassify(artist, genre, lyric_address, lyric_name)
