import webbrowser
import requests
import time

domains = ["facebook.com", #/nickname
"youtube.com", #/@nickname
"instagram.com", #/nickname
"tiktok.com", #/@nickname
"snapchat.com", #/add/nickname
"twitter.com", #/nickname
"ru.pinterest.com",
"reddit.com",
"linkedin.com",
"quora.com",
"discord.com", # discord lookup tool is more appropirate here
"twitch.tv",
"tumblr.com",
"threads.net",
"mastodon.social",
"bsky.app",
"ok.ru",
"vk.com",
"deviantart.com",
"imgur.com"]

slash_domains = ["facebook.com/", "instagram.com/", "twitter.com/", "twitch.tv/", "tumblr.com/", "vk.com/", "shikimori.one/", "bit.ly/", "clck.ru/", "cutt.ly/"] #problems with: "pinterest.com/",
at_domains = ["youtube.com/@", "tiktok.com/@", "threads.net/@", "mastodon.social/@", ]
other_domains = ["snapchat.com/add/", "reddit.com/user/", #"linkedin.com/in/",
                  "quora.com/profile/", "discordlookup.com/user/", "bsky.app/profile/", "ok.ru/profile/", "deviantart.com/", "imgur.com/user/"]

user_domains = slash_domains + at_domains + other_domains

def check_website_content(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the HTTP status code is 200 (OK)
        if response.status_code == 200:
            return True
        else:
            print("Failed to retrieve content: Status code", response.status_code)
            return False
    except requests.RequestException as e:
        print("An error occurred:", e)
        return False

mode = input("Choose mode: 1 - search by username, 2 - search by key word: ")

if mode == "1":
    username = input("Input username to search on social networks: ")
    for domain in user_domains:
        print(domain)
        search_template = "https://www." + domain + username
        if check_website_content(search_template):
            webbrowser.open("https://www." + domain + username)
        else:
            print("Content does not exist!")
            
else: #TODO: fix this mode, bcs it can't find existing links from the mode 1
    keyword = input("Input keyword to search on social networks: ")

    searches = []
    for domain in domains:
        search_template = "\""+keyword+"\" inurl:"+domain
        search_template = search_template.replace(" ", "+")
        searches.append(search_template)

    for search_string in searches:
        webbrowser.open("https://www.google.com/search?q=" + search_string + "&start=" + str(search_string))
        time.sleep(1)
