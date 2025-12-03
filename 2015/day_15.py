import pandas as pd
import json

# input string json
input_ = open(file="day_15.txt", mode='r').read()

#parse
ing = json.loads(input_)
df_ing = pd.DataFrame(ing)


def get_properties_value(prop: str, spoons: int) -> int:
    val = (df_ing[prop]*spoons).sum()
    if val < 0:
        return 0
    else:
        return val
