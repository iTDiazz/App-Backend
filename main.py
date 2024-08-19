from fastapi import FastAPI

app = FastAPI(
    title='Trading App'
)

code = 'uvicorn Project.fastapi.main:app --reload'

fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'investor', 'name': 'Kai'},
    {'id': 3, 'role': 'trader', 'name': 'John'}
]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


fake_trades = [
    {'id_operation': 1, 'wallet': 'MoneyBank', 'crypto_money': 'BTC'},
    {'id_operation': 2, 'wallet': 'CryptoBank', 'crypto_money': 'ETH'},
    {'id_operation': 3, 'wallet': 'RichBank', 'crypto_money': 'TON'},
    {'id_operation': 4, 'wallet': 'BigBank', 'crypto_money': 'NOT'}
]


@app.get('/trades')
def get_trades(limit: int = 0, offset: int = 0):
    return fake_trades[limit:][:offset]


fake_users1 = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'investor', 'name': 'Kai'},
    {'id': 3, 'role': 'trader', 'name': 'John'}
]


@app.post('/')
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get('id') == user_id, fake_users1))[0]
    current_user['name'] = new_name
    return {'status': 200, 'data': current_user}