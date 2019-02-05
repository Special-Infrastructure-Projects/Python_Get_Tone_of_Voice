def get_tone(message):
	sent = open("data.txt","r").read().split("\n")
	positive_common = {}
	negative_common = {}
	for x in range(len(sent)-1):
		row = sent[x].split("\t")
		sentence = row[0]
		score = row[1]
		if score == "1":
			words = sentence.split(" ")
			for y in range(len(words)):
				if words[y] not in positive_common:
					positive_common[words[y]] = 1
				else:
					positive_common[words[y]]+=1
		else:
			words = sentence.split(" ")
			for y in range(len(words)):
				if words[y] not in negative_common:
					negative_common[words[y]] = 1
				else:
					negative_common[words[y]]+=1					
	tmessage = message.split(" ")
	positive_count = 0 	
	positive_occurances = 0
	pos_len = len(positive_common.keys())
	negative_count = 0 
	negative_occurances = 0
	neg_len = len(negative_common.keys())
	for x in range(len(tmessage)):	
		if tmessage[x] in positive_common:	
			positive_count+=1			
			positive_occurances = positive_occurances + positive_common[tmessage[x]]			
		if tmessage[x] in negative_common:		
			negative_count+=1			
			negative_occurances = negative_occurances + negative_common[tmessage[x]]			
	positive_score = (positive_count + positive_occurances / pos_len)*100			
	negative_score = (negative_count + negative_occurances / neg_len)*100					
	score = [1,0]		
	results = [positive_score,negative_score]
	return score[results.index(max(results))]

sentence = "YOUR SENTENCE"	
	
f = get_tone(sentence)
