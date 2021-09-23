#Forum site - https://transcripts.foreverdreaming.org/viewforum.php?f=574
#Episodes-
#https://transcripts.foreverdreaming.org/viewtopic.php?f=574&t=[[25301-25498]]
import requests, bs4, re, pickle
mainSite = requests.get("https://transcripts.foreverdreaming.org/viewforum.php?f=574")
epIndex = 25301
#for i in range(0,197):
#while epIndex <= 25498:
betweenP = re.compile(r"/a*<\s*p[^>]*>(.*?)<\s*/\s*p>/g")
betweenStrong = re.compile(r"/<\s*strong[^>]*>(.*?)<\s*/\s*strong>/g")
#Episode stuuuuuuff
episodeData = {}
characterLines = {}
#Save to files incase something happens to the forums
#{sceneNum, sceneData}
#sceneData = lineData --> {lineIndex: [name,line]}


#Remove scene format, add all lines as seperate lines into an array, maybe
#parse speaker later.

scenes = {}
character_lines = {}
debug_statements = False
testing = True
def seperateMultipleNames(line):
    if "&" in line:
        split = line.split("&")
    elif "and" in line:
        split = line.split("and")

    for count,char in enumerate(split):
        split[count] = char.strip()
    #print(first_name + ","+ second_name)
    return split

def addNamesToDict():
    return
def downloadScript():
    while epIndex <= 25498:
        try:
            current_episode = requests.get("https://transcripts.foreverdreaming.org/viewtopic.php?f=574&t=" + str(epIndex))
            soupEp = bs4.BeautifulSoup(current_episode.text, 'html.parser')
            epText = soupEp.find_all("div",class_="postbody")
            bodyWithTags = str(epText[0])[367:]
            strippedText = epText[0].text.strip()
            strippedLines = strippedText.splitlines()
            i = 1
            for line in strippedLines:
                try:
                    if len(line) > 1:
                        #tempList = line.copy().split(":")
                        """
                        y = line.index(":")
                        name = line[:y]
                        splitLine = line[y+2:]
                        """
                        names = seperateMultipleNames(line)
                        
                        #if not name in characterLines.keys():
                            #characterLines[name] = [splitLine]
                        #else:
                            #characterLines[name].append(splitLine)
                        #print("--Line:",line,"\n----Name:",name,"\n------Quote",
                        #      splitLine)
                        #lineData =[name,splitLine]
                        #scene.append(lineData)
                        for name in names:
                            if name in character_lines.keys():
                                character_lines[name].append(splitLine)
                            else:
                                character_lines[name] = []
                        i+=1
                        #characterLines[tempList[0]] = tempList[1]
                    else:
                        continue
                except Exception as e:
                    if(debug_statements):
                        print("!!!!!!!!!",line,"!!!!!!", e,"!!!!!!!!!!")
                    pass
            
            epIndex+=1
            
        except Exception as e:
            print(f"Error Getting transcript{epIndex}:::{e}")

    
def printLines(d):
    for k,v in d.items():
        print(k,v)

        
def printScenes():
    i=1
    for s in scenes.keys():
        print("Scene:",s)
        for data in scenes[s]:
            print("Name:",data[0],"\n----Line",data[1])
        #for l in scenes[s]:
            #print("L in scene:",l)
            #print("--Name:", scenes[s][l][0],"\n----Line:",scenes[s][l][1])
        i+= 1

        
if(debug_statements):
    printLines()
    print(epIndex)
if not testing:
    character_lines = pickle.load(open("/Users/brandon/Documents/Code/Python/TypingBot/character_dict.p","rb"))
    print("Saved Character Lines")
#for count, key  in enumerate(character_lines.keys()):
 #   print(key)
    #print(count)
#print(character_lines["Pam"][-500:])

#pickle.dump(character_lines, open("/Users/brandon/Documents/Code/Python/TypingBot/character_dict.p","wb"))
#for k in scenes.keys():
    #print("K:",k,"V:",scenes[k])
    
