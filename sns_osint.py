from selenium import webdriver

browser_type = input("Choose browser: 1 - Chrome, 2 - Firefox: ")

if browser_type == "1":
	options = webdriver.ChromeOptions()
	driver = webdriver.Chrome(options=options)
else:
	options = webdriver.FirefoxOptions()
	browser = webdriver.Firefox(options=options)

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

slash_domains = ["facebook.com/", "instagram.com/", "twitter.com/", "pinterest.com/", "twitch.tv/", "tumblr.com/", "vk.com/"]
at_domains = ["youtube.com/@", "tiktok.com/@", "threads.net/@", "mastodon.social/@", ]
other_domains = ["snapchat.com/add/", "reddit.com/user/", "linkedin.com/in/",
                  "quora.com/profile/", "discordlookup.com/user/", "bsky.app/profile/", "ok.ru/profile/", "deviantart.com/", "imgur.com/user/"]

user_domains = slash_domains + at_domains + other_domains

mode = input("Choose mode: 1 - search by username, 2 - search by key word: ")

if mode == "1":
    username = input("Input username to search on social networks: ")
	
    for domain in user_domains:
        browser.get("https://www." + domain + username)
        browser.switch_to.new_window('tab')
    
else:
    keyword = input("Input keyword to search on social networks: ")

    searches = []
    for domain in domains:
        search_template = "\""+keyword+"\" inurl:"+domain
        search_template = search_template.replace(" ", "+")
        searches.append(search_template)

    for search_string in searches:
        browser.get("https://www.google.com/search?q=" + search_string + "&start=" + str(search_string))
        browser.switch_to.new_window('tab')