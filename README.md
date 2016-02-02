# ipytelegram
IPython magic for Telegram notifications

Requires
-------------
    pip install telepot

Install
-------------
    %install_ext https://raw.githubusercontent.com/kalaidin/ipytelegram/master/ipytelegram.py

Load
-------------
    %load_ext ipytelegram

Initialize
-------------
    %telegram_setup <token> <your id>

Use
-------------
Cell magic as follows:

    %%telegram_send I am finally done!
    model.train(epochs=1e10)

will send "I am done" to you on behalf of your bot.

Token
-------------
Talk to [BotFather](https://telegram.me/botfather) to create a bot.

ID
-------------
Send a message to your bot first, then run:

    import telepot
    bot = telepot.Bot(<token>)
    response = bot.getUpdates()

Look up `response` for ID.