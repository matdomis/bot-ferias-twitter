from time import sleep
import logging
import os
import tweepy
import datetime
import schedule

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s"
    " (%(module)s:%(funcName)s:%(lineno)d) %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
    handlers=[stream_handler],
)

logger = logging.getLogger("bot")



#Auth

client = tweepy.Client(
    bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_KEY_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
)


emojis = [
    "¯\\_(ツ)_/¯ BOAS FÉRIAS ESTUDANTE ¯\\_(ツ)_/¯",
    "(*＾▽＾)／",
    "(*^▽^*)",
    "(/^▽^)/",
    "(⌒▽⌒)☆",
    "೭੧(❛▿❛✿)੭೨",
    "☜(⌒▽⌒)☞",
    "ヾ(*´∀｀*)ﾉ",
    "Ψ(　ﾟ∀ﾟ)Ψ",
    "=͟͟͞͞( ✌°∀° )☛",
    "(*≧▽≦) DALE!!!! (^∇^)"
]


# Código
def tweet_remaining_days():
    today = datetime.date.today()
        
    logger.info("Tweeting...")
    vacation = datetime.date(2024, 12, 14)

    nextperiod = datetime.date(2025, 2, 17)
    diffvacationdays = nextperiod - vacation
    vacationdays = diffvacationdays.days

    diff = vacation - today
    days = diff.days

    if (days < 0):
        return;

    if (days == 100):
        client.create_tweet(text="Faltam 💯 dias para as férias! 💪🤓📖")

    elif (days == 69):
        client.create_tweet(text="Faltam {} dias para as férias... 🔥😳😈".format(days))
    elif (days == 50):
        client.create_tweet(text="Faltam {} dias para as férias!! 💪😬☝".format(days))

    elif (days > 10 and days % 10 == 0):
        client.create_tweet(text="Faltam {} dias para as férias da UFPR!! ¯\\_(ツ)_/¯".format(days))

    elif (days > 10):
        client.create_tweet(text="Faltam {} dias para as férias da UFPR".format(days))

    # Começa contagem regressiva!!
    elif (days <= 10 and days > 1):
        client.create_tweet(text="Faltam {} dias para as férias!!! {}".format(days, emojis[days]))

    elif (days == 1):
        client.create_tweet(text="Falta {} dia para as férias da UFPR {}".format(days, emojis[days]))

    elif (days == 0):
        client.create_tweet(text="¯\\_(ツ)_/¯ BOAS FÉRIAS ESTUDANTE ¯\\_(ツ)_/¯")
        client.create_tweet(text="Teremos {} dias de férias.".format(vacationdays))
        client.create_tweet(text="Atenção, esse robôzinho aqui está de férias 🍺🌅🍻, até o próximo período.")

logger.info("Starting bot...")
schedule.every().day.at("12:00").do(tweet_remaining_days)

while True:
    schedule.run_pending()
    sleep(1)
