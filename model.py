import json

def save_msg(link, msg):
	messages = get_msgs()
	messages[link] = msg
	with open('msgs.json', 'w') as f:
		f.write(json.dumps(messages))
		f.close()
	
def delete_msg(link):
	messages = get_msgs()
	del messages[link]
	with open('msgs.json', 'w') as f:
		f.write(json.dumps(messages))
		f.close()

def get_msgs():
	f = open('msgs.json', 'r')
	return json.loads(f.read())