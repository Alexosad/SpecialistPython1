# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

# TODO: your code here

month = int(input("m: "))
if 0<month<=2 or month==12:
	print("winter")
if 2<month<=5:
	print("spring")
if 5<month<=8:
	print ("summer")
if 8<month<=11:
	print ("autumn")
else:
	print ("")
