def tabulateFrames(rawScores):
	#Loop through the input array and make it more manageable to work with
	scores = []
	for n in range(len(rawScores)):
		if rawScores[n] == 'X':
			scores.append(10)
		elif rawScores[n] == '/':
			scores.append('/')
		else:
			scores.append(int(rawScores[n]))
	
	#Initialization
	result = []
	currentFrame = 0
	i = 0

	#Handle each frame before the 10th with one ruleset:
	while currentFrame < 9 and i < len(scores):
		#spare logic
		if i + 1 < len(scores) and scores[i + 1] == '/':
			if i + 2 < len(scores):
				result.append(10 + scores[i + 2])
			else:
				result.append(None)
			currentFrame += 1
			i += 2
		#strike logic
		elif scores[i] == 10:
			if i + 2 < len(scores):
				#handle strike bonus scoring
				nextroll = scores[i + 1]
				nextnextroll = scores[i + 2] if scores[i + 2] != '/' else (10 - nextroll) 
				result.append(scores[i] + nextroll + nextnextroll)
			else:
				result.append(None)
			i += 1
			currentFrame += 1
     	#integer roll logic
		else:
			if i + 1 < len(scores):
				result.append(scores[i] + scores[i + 1])
				currentFrame += 1
				i += 2
			else:
				result.append(None)
				currentFrame += 1

	#Handle the 10th frame with separate rules:
	if currentFrame == 9 and i < len(scores):
		#handle spare
		if i + 1 < len(scores) and scores[i + 1] == '/':
			if i + 2 < len(scores):
				result.append(10 + scores[i + 2])
			else:
				result.append(None)
		#handle strike
		if scores[i] == 10:
			if i + 2 < len(scores):
				nextroll = scores[i + 1]
				nextnextroll = scores[i + 2] if scores[i + 2] != '/' else (10 - nextroll)
				result.append(scores[i] + nextroll + nextnextroll)
			else:
				result.append(None)
		#handle integer rolls
		else:
			if i + 1 < len(scores):
				if scores[i + 1] == '/':
					if i + 2 < len(scores):
						result.append(scores[i] + (10 - scores[i]) + scores[i + 2])
					else:
						result.append(None)
				else:
					result.append(scores[i] + scores[i + 1])
			else:
				result.append(None)
		
	#fill the result array if we have an incomplete game
	while len(result) < 10:
		result.append(None)

	return result

# Test Cases
example = ['4', '5', 'X', '8', '1']
print('Input: ' + str(example))
print('Expected output: [9, 19, 9, None, None, None, None, None, None, None]')
print('Result: ' + str(tabulateFrames(example)))

alice_scores = ['X', '7', '/', '9', '0', 'X', '0', '8', '8', '/', '0', '6', 'X', 'X', 'X', '8', '1']
print('Input: ' + str(alice_scores))
print('Expected output: [20, 39, 48, 66, 74, 84, 90, 120, 148, 167]')
print('Result: ' + str(tabulateFrames(alice_scores)))


bob_scores = ['9', '0', 'X', '7', '/', 'X', '9', '/', 'X', 'X', '0', '7', '8', '/', '9', '/', 'X']
print('Input: ' + str(bob_scores))
print('Expected output: [9, 26, 46, 65, 84, 104, 121, 141, 158, 178]')
print('Result: ' + str(tabulateFrames(bob_scores)))


charlie_scores = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
#print('Input: ' + str(charlie_scores))
#print('Expected output: [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]')
#print('Result: ' + str(tabulateFrames(charlie_scores)))


diana_scores = ['8', '/', '7', '/', '7', '2', '9', '/', 'X', 'X', '8', '/', 'X', '9', '/', 'X', '9', '/']
#print('Input: ' + str(diana_scores))
#print('Expected output: [17, 34, 43, 63, 91, 108, 128, 148, 167, 187]')
#print('Result: ' + str(tabulateFrames(diana_scores)))


edward_scores = ['X', '8', '/', '5', '3', 'X', 'X', '9', '/', 'X', '6', '/', '8', '1', '7', '/', 'X']
#print('Input: ' + str(edward_scores))
#print('Expected output: [20, 35, 43, 73, 93, 113, 132, 151, 170, 180]')
#print('Result: ' + str(tabulateFrames(edward_scores)))

