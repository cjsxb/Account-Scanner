import requests

print("Currently 6 websites with working functionality. Search -1 to exit loop.")

while True:
    user = input("Username to search for: ")

    if user == "-1":
        exit()

    listWebsites = [
        "https://www.chess.com/member/",
        "https://www.deviantart.com/",
        "https://github.com/",
        "https://www.tumblr.com/",
        "https://www.quora.com/profile/",
        "https://www.youtube.com/@",
        # 200 "https://www.instagram.com/",
        # 200"https://www.facebook.com/",
        # 403 "https://www.snapchat.com/add/",
        # 403 "https://leetcode.com/u/",
        # 200 "https://www.tiktok.com/@",
        # 200 "https://www.twitch.tv/",
        # 999 "https://www.linkedin.com/in/",
        # 200 "https://x.com/"
        # 200 "https://www.reddit.com/user/",
        # 200 "https://www.pinterest.com/",
        # 429 "https://medium.com/@",
    ]

    oks=0
    for link in listWebsites:
        # Concatenate url with each link being looped with the inputted username
        url = f"{link}{user}"
        response = requests.get(url)
        status = response.status_code
        # 200 means the website responded with 'OK' status.
        if status == 200:
            print(f"✔️ {url}")
            oks += 1
        # Something went wrong and there is likely not an account or the website is filtering traffic
        else:
            print(f"❌ {url} returned {status}")

    print(f"Found {oks} matches and {len(listWebsites)-oks} misses \n")
