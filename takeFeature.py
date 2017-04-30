from nltk.tokenize import word_tokenize as wt
import nltk
import csv

JJ_dict = {}
RB_dict = {}
NN_dict = {}
VB_dict = {}

HP_JJ_dict = {}
HP_RB_dict = {}
HP_NN_dict = {}
HP_VB_dict = {}

SD_JJ_dict = {}
SD_RB_dict = {}
SD_NN_dict = {}
SD_VB_dict = {}

artists_dict = {}
HP_artists_dict = {}
SD_artists_dict = {}

genres_dict = {}
HP_genres_dict = {}
SD_genres_dict = {}


with open(r"D:\UTD\Courses\2017Spring\NLP\FinalProject\data.csv", encoding = "utf-8") as myFile:
    reader = csv.DictReader(myFile)
    
    for row in reader:
        #count artist appearence     
        if row["artist"] not in artists_dict:
            artists_dict[row["artist"]] = 1
        else:
            artists_dict[row["artist"]] += 1
        
        #count artist appearence under happy mood
        if row["mood"] == "happy":
            if row["artist"] not in HP_artists_dict :
                HP_artists_dict[row["artist"]] = 1
            else:
                HP_artists_dict[row["artist"]] += 1
        
        #count artist appearence under happy mood
        if row["mood"] == "sad":
            if row["artist"] not in SD_artists_dict :
                SD_artists_dict[row["artist"]] = 1
            else:
                SD_artists_dict[row["artist"]] += 1
        
        #count genre appearence
        if row["genre"] not in genres_dict:
            genres_dict[row["genre"]] = 1
        else:
            genres_dict[row["genre"]] += 1
        
        #count genre appearence under happy mood
        if row["mood"] == "happy":
            if row["genre"] not in HP_genres_dict :
                HP_genres_dict[row["genre"]] = 1
            else:
                HP_genres_dict[row["genre"]] += 1
                
        #count genre appearence under sad mood
        if row["mood"] == "sad":
            if row["genre"] not in SD_genres_dict :
                SD_genres_dict[row["genre"]] = 1
            else:
                SD_genres_dict[row["genre"]] += 1
                
        wt_lyric = wt(row["lyrics"])
        pt_lyric = nltk.pos_tag(wt_lyric)
        #print (pt_lyric)
        loel = len(wt_lyric)
        
        #count adjective appearence under all condition
        for n in range(loel): 
            if (pt_lyric[n][1] in ["JJ", "JJR", "JJS"]):
                
                if pt_lyric[n][0] not in JJ_dict:
                    JJ_dict[pt_lyric[n][0]]=1
                else:
                    JJ_dict[pt_lyric[n][0]] += 1
        
        #count adverbe appearence under all condition
        for n in range(loel): 
            if (pt_lyric[n][1] in ["RB", "RBR", "RBS"]):
                
                if pt_lyric[n][0] not in RB_dict:
                    RB_dict[pt_lyric[n][0]]=1
                else:
                    RB_dict[pt_lyric[n][0]] += 1
        
        #count noun appearence under all condition
        for n in range(loel): 
            if (pt_lyric[n][1] in ["NN", "NNS", "NNP", "NNPS"]):
                
                if pt_lyric[n][0] not in NN_dict:
                    NN_dict[pt_lyric[n][0]]=1
                else:
                    NN_dict[pt_lyric[n][0]] += 1
        
        #count verb appearence under all condition            
        for n in range(loel): 
            if (pt_lyric[n][1] in ["VB", "VBD", "VBZ", "VBN", "VBP", "VBG"]):
                
                if pt_lyric[n][0] not in VB_dict:
                    VB_dict[pt_lyric[n][0]]=1
                else:
                    VB_dict[pt_lyric[n][0]] += 1
        
        #count adjective/adverbe/noun/verb appearence under happy emotion:
        if row["mood"] == "happy":
            for n in range(loel): 
                if (pt_lyric[n][1] in ["JJ", "JJR", "JJS"]):
                    
                    if pt_lyric[n][0] not in HP_JJ_dict:
                        HP_JJ_dict[pt_lyric[n][0]]=1
                    else:
                        HP_JJ_dict[pt_lyric[n][0]] += 1
            
            for n in range(loel): 
                if (pt_lyric[n][1] in ["RB", "RBR", "RBS"]):
                    
                    if pt_lyric[n][0] not in HP_RB_dict:
                        HP_RB_dict[pt_lyric[n][0]]=1
                    else:
                        HP_RB_dict[pt_lyric[n][0]] += 1
                        
            for n in range(loel): 
                if (pt_lyric[n][1] in ["NN", "NNS", "NNP", "NNPS"]):
                    
                    if pt_lyric[n][0] not in HP_NN_dict:
                        HP_NN_dict[pt_lyric[n][0]]=1
                    else:
                        HP_NN_dict[pt_lyric[n][0]] += 1
                        
            for n in range(loel): 
                if (pt_lyric[n][1] in ["VB", "VBD", "VBZ", "VBN", "VBP", "VBG"]):
                    
                    if pt_lyric[n][0] not in HP_VB_dict:
                        HP_VB_dict[pt_lyric[n][0]]=1
                    else:
                        HP_VB_dict[pt_lyric[n][0]] += 1
            #print (JJ_dict)
        
        #count adjective/adverbe/noun/verb appearence under sad emotion:
        if row["mood"] == "sad":
            for n in range(loel): 
                if (pt_lyric[n][1] in ["JJ", "JJR", "JJS"]):
                    
                    if pt_lyric[n][0] not in SD_JJ_dict:
                        SD_JJ_dict[pt_lyric[n][0]]=1
                    else:
                        SD_JJ_dict[pt_lyric[n][0]] += 1
            
            for n in range(loel): 
                if (pt_lyric[n][1] in ["RB", "RBR", "RBS"]):
                    
                    if pt_lyric[n][0] not in SD_RB_dict:
                        SD_RB_dict[pt_lyric[n][0]]=1
                    else:
                        SD_RB_dict[pt_lyric[n][0]] += 1
                        
            for n in range(loel): 
                if (pt_lyric[n][1] in ["NN", "NNS", "NNP", "NNPS"]):
                    
                    if pt_lyric[n][0] not in SD_NN_dict:
                        SD_NN_dict[pt_lyric[n][0]]=1
                    else:
                        SD_NN_dict[pt_lyric[n][0]] += 1
                        
            for n in range(loel): 
                if (pt_lyric[n][1] in ["VB", "VBD", "VBZ", "VBN", "VBP", "VBG"]):
                    
                    if pt_lyric[n][0] not in SD_VB_dict:
                        SD_VB_dict[pt_lyric[n][0]]=1
                    else:
                        SD_VB_dict[pt_lyric[n][0]] += 1

sorted_JJ = sorted(JJ_dict.items(), key = lambda x:x[1])
sorted_RB = sorted(RB_dict.items(), key = lambda x:x[1])
sorted_NN = sorted(NN_dict.items(), key = lambda x:x[1])
sorted_VB = sorted(VB_dict.items(), key = lambda x:x[1])

sorted_HP_JJ = sorted(HP_JJ_dict.items(), key = lambda x:x[1])
sorted_HP_RB = sorted(HP_RB_dict.items(), key = lambda x:x[1])
sorted_HP_NN = sorted(HP_NN_dict.items(), key = lambda x:x[1])
sorted_HP_VB = sorted(HP_VB_dict.items(), key = lambda x:x[1])

sorted_SD_JJ = sorted(SD_JJ_dict.items(), key = lambda x:x[1])
sorted_SD_RB = sorted(SD_RB_dict.items(), key = lambda x:x[1])
sorted_SD_NN = sorted(SD_NN_dict.items(), key = lambda x:x[1])
sorted_SD_VB = sorted(SD_VB_dict.items(), key = lambda x:x[1])

