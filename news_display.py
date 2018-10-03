import requests
import json 
import sys
import os
import threading

class NewsThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)
 
    def run(self):
        self._target(*self._args)
 

def display_news_based_on_source(source):
	API_KEY = "{your newsapi.org API key }"
	News = requests.get("https://newsapi.org/v2/top-headlines?sources="+str(source)+"&apiKey="+str(API_KEY))
	FilePath = os.getcwd() + "/" + source + ".txt"
	NewsJson =  json.loads(News.content)
	with open(FilePath,"wb") as f:
		for article in NewsJson["articles"]:
			f.write("Author : " + article["author"].encode('utf-8') )
			f.write("\n")
			f.write("-------------------------")
			f.write("\n")
			f.write("PublishedAt : " + article["publishedAt"].encode('utf-8'))
			f.write("\n")
			f.write("-------------------------")
			f.write("\n")
			f.write("Description : " + article["description"].encode('utf-8'))
			f.write("\n")
			f.write("-------------------------")
			f.write("\n")
			f.write("Content : " + article["content"].encode('utf-8'))
			f.write("\n")
			f.write("-------------------------")
			f.write("\n")
			f.write("Url : " + article["url"].encode('utf-8'))



def display_news_based_on_category(Category):
	News = requests.get("http://127.0.0.1:9005/news?category="+str(Category))
	#f.write(News
	NewsJson = json.loads(News.content)["data"]
	#f.write(NewsJson
	FilePath = os.getcwd() + "/" + Category + ".txt"
	with open(FilePath,"wb") as f:
		for n in NewsJson:
			f.write("Author : "+n["author"].encode('utf-8'))
			f.write("\n")
			f.write("-------------------------")
			f.write("\n")
			f.write("Date : "+ n["date"].encode('utf-8') + " Time: "+n["time"].encode('utf-8'))
			f.write("\n")
			f.write("-------------------------")
			f.write("\n")
			f.write(n["content"].encode('utf-8'))
			f.write("\n")
			f.write("-------------------------")
			f.write("\n")
			f.write("ReadMoreUrl : "+ n["readMoreUrl"].encode('utf-8'))
			f.write("\n")
			f.write("-------------------------")
			f.write("\n")
			f.write("url : " + n["url"].encode('utf-8'))
			f.write("\n")
			f.write("-----------------------------------------")
			f.write("\n")

if __name__ == "__main__":
	
	Categorylist = ["world","technology","national","science","politics","startup"]
	NewsThreads = []
	#print "cron started"
	for Category in Categorylist:
		t = NewsThread(display_news_based_on_category,Category)
		NewsThreads.append(t)
	for thread in NewsThreads:
		thread.start()
	for thread in NewsThreads:
		thread.join()


