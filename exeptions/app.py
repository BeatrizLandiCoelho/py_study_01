try:
    number = int(input("digite um numero: "))
    print(number)

    10/0
except ZeroDivisionError:
    print("you cannor divie this by zero")

except ValueError:
    print("value error")

except:
    print("print a valid number")

#finaly fecha o arquivo
finally:
    print("sempre executa")

