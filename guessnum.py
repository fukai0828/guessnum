# 產生一個隨機整數1~100（不要印出來）
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了！"
# 猜錯的話 要告訴他 比答案大還是小

import random

r = random.randint (1, 100)
while True:
	num = input('請猜數字:')
	num = int(num)
	if num == r:
		print('你猜中了！')
		break
	elif num > r:
		print('再小一點')
	elif num < r:
		print('再大一點')

