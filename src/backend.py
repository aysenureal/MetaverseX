import tweepy
import random
import time
from web3 import Web3


API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_SECRET = "YOUR_ACCESS_SECRET"

# Web3 Bağlantısı
INFURA_URL = "YOUR_INFURA_URL"
CONTRACT_ADDRESS = "YOUR_CONTRACT_ADDRESS"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Web3, yatırım, FOMO anahtar kelimeleri
KEYWORDS = ["Web3", "crypto", "token", "bull run", "FOMO", "rug pull"]

# Oyun için örnek sorular
QUESTIONS = [
    {"question": "Bitcoin 1 saat içinde yükselir mi?", "answer": "yes"},
    {"question": "ETH yarına kadar 5% artar mı?", "answer": "no"},
    {"question": "Şu an X token almak mantıklı mı?", "answer": "yes"}
]

def find_and_mention():
    tweets = api.search_tweets(q=random.choice(KEYWORDS), count=10, lang='en')
    for tweet in tweets:
        question = random.choice(QUESTIONS)
        mention_text = f"@{tweet.user.screen_name} {question['question']} Cevabın 'yes' veya 'no'! 30 saniyen var!" 
        api.update_status(mention_text, in_reply_to_status_id=tweet.id)
        time.sleep(30)  # 30 saniye bekle
        check_answer(tweet.user.screen_name, question)

def check_answer(user, question):
    print(f"Checking answer for {user}...")
    correct = question['answer']
    result_text = f"@{user} Doğru cevap: {correct}! {('Kazandın 🎉' if correct == 'yes' else 'Kaybettin 😢')}"
    api.update_status(result_text)
    if correct == "yes":
        send_reward(user)

def send_reward(user):
    account = w3.eth.account.from_key(PRIVATE_KEY)
    tx = {
        'to': CONTRACT_ADDRESS,
        'value': w3.to_wei(0.01, 'ether'),
        'gas': 21000,
        'gasPrice': w3.to_wei('50', 'gwei'),
        'nonce': w3.eth.get_transaction_count(account.address),
    }
    signed_tx = account.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Sent reward to {user}, Tx Hash: {tx_hash.hex()}")

while True:
    find_and_mention()
    time.sleep(300) 
