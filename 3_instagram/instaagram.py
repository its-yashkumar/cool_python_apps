from instabot import Bot
bot = Bot()
bot.login(username="PYInsta_Bot_99", password="PythonProject")

######  upload a picture #######
# bot.upload_photo("computer.jpg", caption="computer")

######  follow someone #######
bot.follow("vinayak_dixit_7707_")

######  send a message #######
bot.send_message("Hello from Me", ['yashkumar_jain_62'])

######  get follower info #######
my_followers = bot.get_user_followers("dhavalsays")
for follower in my_followers:
    print(follower)

#bot.unfollow_everyone()
