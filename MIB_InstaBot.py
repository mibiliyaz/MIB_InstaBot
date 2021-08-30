from instabot import Bot
bot = Bot()
bot.login(username = "mib_instabot_demo", password = "********") #here ******* are my password
bot.follow("ieeemjcet_cis")
bot.upload_photo("MIB.jpg", caption = "Its me, your MIB")
bot.send_message("Hi I am a bot","iam_iliyaz")
bot.get_user_followers('iam_iliyaz')
bot.get_user_following("iam_iliyaz")
bot.unfollow("ieeemjcet_cis")
