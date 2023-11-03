x = set(input(' Player 1 masukkan lima huruf alphabet yang anda inginkan : ').split(','))
y = set(input(' Player 2 masukkan lima huruf alphabet yang anda inginkan : ').split(','))

zxc = x.intersection(y)
print('Kesamaan alphabet favorit dengan player 2 adalah {}'.format((len(zxc)/len(x))*100))