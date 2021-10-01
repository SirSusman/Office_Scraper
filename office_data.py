#Forum site - https://transcripts.foreverdreaming.org/viewforum.php?f=574
#Episodes-
#https://transcripts.foreverdreaming.org/viewtopic.php?f=574&t=[[25301-25498]]
import requests, bs4, re, pickle, time
mainSite = requests.get("https://transcripts.foreverdreaming.org/viewforum.php?f=574")
epIndex = 25301
#311 - Good
test_stop = 25460
test_start = 25440



test_ep = 25459
betweenP = re.compile(r"/a*<\s*p[^>]*>(.*?)<\s*/\s*p>/g")
betweenStrong = re.compile(r"/<\s*strong[^>]*>(.*?)<\s*/\s*strong>/g")

scenes = {}
character_lines = {}
debug_statements = False
testing = True
saving = False


def seperateMultipleNames(line):

    #Remake with regex
    #Characters to remove from name
    badCharacters = "[]\'\""
    names = []
    name_arr = []
    name = ""
    if ":" in line[:20]:
        splitLine = line.split(":")[-1].strip()
        names = line.split(":")[0].strip()
    else:
        return




    seperators = ["&"," and ", ",","/"]
    for s in seperators:
        if s in names:
            #print(f"{s}, is in {names}.")
            name_arr = names.split(s)

    """
    if "&" in names or " and " in names or "," in names or "/" in names:
        name_arr = names.split("&")
    elif :
        name_arr = names.split("and")
    elif :
        name_arr = names.split(',')
    elif :
        name_arr = names.split("/")
    """
    
        
    
    
    if len(name_arr)>0:
        name_arr[-1] = name_arr[-1].split(":")[0]
        for count,char in enumerate(name_arr):
            name_arr[count] = char.strip()
    #print(first_name + ","+ second_name)
    splitLine = line.split(":")[-1].strip()
    
    if len(name_arr) > 0:
        for name in name_arr:
            name = line.split(":")[0].strip().lower().replace(character,"")
            if name in character_lines.keys():
                character_lines[name].append(splitLine)
            else:
                character_lines[name.strip()] = [splitLine]
    else:
        name = line.split(":")[0].strip().lower()
        if name in character_lines.keys():
            character_lines[name].append(splitLine)
        else:
            character_lines[name] = [splitLine]
    
    if(debug_statements):
        print("Names Array:")
        print(name_arr)
        print("================")
        print("Actual Line: ")
        print(splitLine)
        print("==============")
        print("Names: " + names)
        print("\n\n")

    return

def addNamesToDict(names):
        
    return

def downloadEpisode(epIndex):
    current_episode = requests.get("https://transcripts.foreverdreaming.org/viewtopic.php?f=574&t=" + str(epIndex))
    soupEp = bs4.BeautifulSoup(current_episode.text, 'html.parser')
    epText = soupEp.find_all("div",class_="postbody")
    bodyWithTags = str(epText[0])[367:]
    strippedText = epText[0].text.strip()
    strippedLines = strippedText.splitlines()
    i = 1

    #NOT GRABBING LINE FROM MULTIPLE NAMES


    for line in strippedLines:
        try:
            if len(line) > 1:
                #tempList = line.copy().split(":")
                """
                y = line.index(":")
                name = line[:y]
                        splitLine = line[y+2:]
                        """
                seperateMultipleNames(line)
                        
                        #if not name in characterLines.keys():
                            #characterLines[name] = [splitLine]
                        #else:
                            #characterLines[name].append(splitLine)
                        #print("--Line:",line,"\n----Name:",name,"\n------Quote",
                        #      splitLine)
                        #lineData =[name,splitLine]
                        #scene.append(lineData)
                        #if(len(names)>0):
                        #    addNamesToDict(names)
                        
                i+=1
                        #characterLines[tempList[0]] = tempList[1]
            else:
                continue
        except Exception as e:
            if(debug_statements):
                print("!!!!!!!!!",line,"!!!!!!", e,"!!!!!!!!!!")
            pass


def downloadScript(epIndex,stop):
    #25498
    
    if(not testing):
        stop = 25498


    while epIndex <= stop:
        try:
            downloadEpisode(epIndex)
            
            epIndex+=1
            
        except Exception as e:
            print(f"Error Getting transcript{epIndex}:::{e}")

def printKeys():
    for key in character_lines.keys():
        print(":::::"+key + ":::::")

        
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




if testing:
    #downloadScript(test_start,test_stop)
    #downloadEpisode(test_ep)
    character_lines = pickle.load(open("/Users/brandon/Documents/Code/Python/TypingBot/character_dict.p","rb"))
    #pickle.dump(character_lines, open("/Users/brandon/Documents/Code/Python/TypingBot/character_dict.p","wb"))
    print(character_lines['michael'])
#for count, key  in enumerate(character_lines.keys()):
 #   print(key)
    #print(count)
#print(character_lines["Pam"][-500:])
if not testing:
    print("Working...")
    downloadScript(epIndex,test_stop)
    if(saving):
        print("Saved")
        pickle.dump(character_lines, open("/Users/brandon/Documents/Code/Python/TypingBot/character_dict.p","wb"))
    #print(character_lines.keys())
    print(character_lines.keys())
#for k in scenes.keys():
    #print("K:",k,"V:",scenes[k])
    
