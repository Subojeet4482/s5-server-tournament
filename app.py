"""SERVER-5  -  user log + account verify: same IP / same device fingerprint creating many accounts   (DB3)"""
from common.appfactory import create_app
from modules import fraud_mod

app = create_app("s5", "Server-5 (fraud / device check)", [fraud_mod], caps=("fraud",), dbs=("DB3",))
