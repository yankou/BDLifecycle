from account_model import Account
import pprint
import json

def preprocessing(line):
	if ", Inc." in line:
		newline = line.replace(", Inc.", "")
		line = newline
	return line

all_accounts = {}

with open('HD.BOSCompanyTracking17ADump.csv','r') as f:
	data = f.readlines()
data = [x.strip() for x in data] 



for line in data:
	newline = preprocessing(line)
	ii = newline.split(',')
	u = Account(ii[1])
	u.add_line(ii)
	if u.company in all_accounts:
		all_accounts[u.company] += u.status
	else:
		all_accounts[u.company] = u.status
print(len(all_accounts))


all_events = {}
all_status = {}
for key, value in all_accounts.iteritems():
	uu = Account(key)
	for val in value:
		uu.add_status(val[0],val[1])
	all_events[key] = uu.getEvents()
	all_status[key] = uu.getStatusMatrix()
	# print(key+": "+str(all_status[key]))
print(len(all_status["Aetna"]))

## Save events data to json
# with open('events_output.json', 'w') as fp:
#     json.dump(all_events, fp)

## Save status to json
with open('status_matrix_output.json', 'w') as fp:
    json.dump(all_status, fp)

