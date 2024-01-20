import sys

def Calculator(num1, operator, num2):
	if operator == '+':
		result = num1 + num2
	elif operator == '-':
		result = num1 - num2
	else:
		print("Nieprawidlowy operator.")
		sys.exit(1)

	with open('/tmp/wynik.txt', 'w') as file:
		file.write(str(result))

if __name__ == "__main__":
	if len(sys.argv) != 4:
		print("uzycie calc.py <liczba_1> <+ lub  -> <liczba_2>")
		sys.exit(1)

	num1=float(sys.argv[1])
	operator = sys.argv[2]
	num2=float(sys.argv[3])

Calculator(num1, operator, num2)
