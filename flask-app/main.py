import dtale
import pandas as pd

from flask import Flask

df = pd.DataFrame([1,2,3,4,5])
dtale.show(
    df,
    port=5030,
    app_root='/user/aschonfeld-binder-flask-app-qrv8kj1c/proxy/5030',
    subprocess=False,
)

