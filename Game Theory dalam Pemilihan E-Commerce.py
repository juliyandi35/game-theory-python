# Game Theory dalam Pemilihan E-Commerce untuk Pemasaran
pip install nashpy

import pandas as pd
import numpy as np
## Read the Excel data
data = pd.read_excel('/content/data penjualan.xlsx')
data

# Julian's payoffs (row player)
x = np.array(data.corr())
# Randy's payoffs (column player)
y = x.T
import nashpy as nash
shopping_dilemma = nash.Game(x,y)
shopping_dilemma

pip install quantecon

import quantecon as qe
# create a list containing both players payoffs
pt = [[(1,1), (-0.60246807,-0.60246807)], [(-0.60246807,-0.60246807), (1,1)]]
g = qe.game_theory.NormalFormGame(pt)
print(g)

# write the payoff function
def payoff_function (x=str, y=str):
    if x == 'Shopee' and y == 'Shopee':
        print('Julian {}'.format(1),':','Randy {}'.format(1))
    elif x == 'Shopee' and y == 'Tiktok':
        print('Julian {}'.format(-0.60246807),':','Randy {}'.format(-0.60246807))
    elif x == 'Tiktok' and y == 'Tiktok':
        print('Julian {}'.format(1),':','Randy {}'.format(1), ':', "NE")
    else:
        print('Julian {}'.format(-0.60246807),':','Randy {}'.format(-0.60246807))

payoff_function('Shopee', 'Tiktok')

payoff_function('Tiktok', 'Tiktok')