# ipytelegram
IPython magic for Telegram notifications,

or get a push once a model is finally trained.

Requires
```
    pip install -r requirements.txt
```

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

    %%telegram_send I am finally trained!
    model.train(epochs=1e10)

will send "I am finally trained!" to you on behalf of your bot once the cell is completed.

Token
-------------
Talk to [BotFather](https://telegram.me/botfather) to create a bot and get a token.

ID
-------------
The bot is not able to start a conversation with you, so talk to him first, then run:

    import telepot
    bot = telepot.Bot(<token>)
    response = bot.getUpdates()

Look up `response` for your ID.