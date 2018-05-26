## File to generate the dataset for SQUAD DATA SET.
## Change the value of the variable 'FILE_LOCATION' to the json file location you want.
## This outputs four text files and four pickle files of same length.


import json
import pickle
from random import shuffle

FILE_LOCATION = 'json_data_files/train-v1.1.json'
prefix ='train'

f=open('data_in_text_files/'+prefix+'_paragraph.txt','w')
g=open('data_in_text_files/'+prefix+'_question.txt','w')
h=open('data_in_text_files/'+prefix+'_answer.txt','w')
e=open('data_in_text_files/'+prefix+'_span.txt','w')

passages,questions,answers,spans = [],[],[],[]

with open(FILE_LOCATION) as q:
	data = json.load(q)

full_dataset =[]

for i in range(len(data['data'])):
	for j in range(len(data['data'][i]['paragraphs'])):

		passage = data['data'][i]['paragraphs'][j]['context']


		for k in range(len(data['data'][i]['paragraphs'][j]['qas'])):

				question = data['data'][i]['paragraphs'][j]['qas'][k]['question']
				answer = data['data'][i]['paragraphs'][j]['qas'][k]['answers'][0]['text']
				start = data['data'][i]['paragraphs'][j]['qas'][k]['answers'][0]['answer_start']
				end = data['data'][i]['paragraphs'][j]['qas'][k]['answers'][0]['answer_start'] + len(answer)
				passage = data['data'][i]['paragraphs'][j]['context']

				span = (start,end)

				while '\n' in passage:
					index = passage.index('\n')
					passage = passage[0:index] + passage[index+1:]

				# f.write(str(passage)+'\n')			
				# g.write(str(question)+'\n')
				# h.write(str(answer)+'\n')
				# e.write(str(start) + ' ' + str(end) + '\n')


				# passages.append(passage)
				# answers.append(answer)
				# questions.append(question)
				# spans.append(span)

				full_dataset.append([passage,question,answer,span])


# f.close()
# g.close()
# h.close()
# e.close()

shuffle(full_dataset)

for passage,question,answer,span in full_dataset:
	f.write(str(passage)+'\n')			
	g.write(str(question)+'\n')
	h.write(str(answer)+'\n')
	e.write(str(span[0]) + ' ' + str(span[1]) + '\n')

	passages.append(passage)
	answers.append(answer)
	questions.append(question)
	spans.append(span)


with open('data_in_pickle_files/'+prefix+'_paragraph.pickle','wb') as h:
	pickle.dump(passages,h)

with open('data_in_pickle_files/'+prefix+'_question.pickle','wb') as h:
	pickle.dump(questions,h)	

with open('data_in_pickle_files/'+prefix+'_answer.pickle','wb') as h:
	pickle.dump(answers,h)	

with open('data_in_pickle_files/'+prefix+'_span.pickle','wb') as h:
	pickle.dump(spans,h)	
