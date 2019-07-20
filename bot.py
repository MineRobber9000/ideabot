import teambot, requests, argparse, shlex
from requests.utils import quote as qr

quote = lambda x: qr(x.encode("utf-8"),safe="")

WORDBOT = "https://api.noopschallenge.com/wordbot"

def get_words(set,count):
	r = requests.get(WORDBOT+"?set={}&count={}".format(quote(set),quote(str(count))))
	r.raise_for_status()
	r = r.json()
	return r["words"]

def get_parser():
	parser = argparse.ArgumentParser(add_help=False)
	parser.add_argument("-h","--help",action="store_true")
	parser.add_argument("-l","--list-sets",action="store_true")
	parser.add_argument("-s","--set",default="common")
	parser.add_argument("count",nargs="?",default=3,type=int)
	return parser

def join_words(words):
	words=['"'+x+'"' for x in words]
	if len(words)==1:
		return words[0]
	elif len(words)==2:
		return " and ".join(words)
	else:
		return (", ".join(words[:-1]))+", and "+words[-1]

class IdeaBot(teambot.Handler):
	def on_pubmsg(self,channel,nick,text):
		if not text.startswith("!idea"): return
		args = text.split(" ",1)
		if len(args)==1:
			args = ""
		else:
			args = args[1]
		p = get_parser()
		args = p.parse_args(shlex.split(args))
		if args.help:
			self.say(channel,"{}: Get some words! Usage: !idea [-s/--set <set>] [count] (`!idea -l` to list sets)".format(nick))
			return
		if args.list_sets:
			try:
				sets = requests.get(WORDBOT+"/sets")
				sets.raise_for_status()
				sets = sets.json()
				self.say(nick,"Sets are: "+", ".join(sets))
				self.say(channel,nick+": PMed!")
			except:
				self.say(channel,"{}: Sorry, I can't get you that right now. Something's wrong...".format(nick))
		try:
			words = get_words(args.set,args.count)
		except:
			self.say(channel,"{}: Sorry, I can't get you that right now. Something's wrong...".format(nick))
		self.say(channel,"{}: How about a story with the word{} {}?".format(nick,"s" if len(words)!=1 else " ".strip(),join_words(words)))

if __name__=="__main__":
	channels = "#writing".split()
	bot = teambot.TeamBot(channels,"ideabot","localhost",chandler=IdeaBot)
	bot.start()
