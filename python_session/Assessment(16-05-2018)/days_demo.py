
days = ["yesterday", "today", "tomorrow", "dayafter"]

count = 0

for day in days:
	print day[:count+1].upper()+day[count+1:]
	count = count+1
