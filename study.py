
## 짝수 프린트

def get_even_number(numbers:list):
    even_numbers = []
    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

print(get_even_number([1,2,3,4,5]))

## 딕셔너리 프린트
def calc(a,b):
    return {"add":a+b,"sub":a-b,"mul":a*b,"div":a/b}

print(calc(10, 2))
print(calc(6, 3))



