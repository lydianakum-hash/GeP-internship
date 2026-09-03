def get_grade(score):
    if score >=90:
        return "A grade"
    elif score >=80:
        return "B grade"
    elif score >=70:
        return "C grade"
    elif score >=60:
        return "D grade"
    else:
        return "F grade"
#list of scores
scores=[95,42,91,76,68]
#display scores and grades
for score in scores:
    print("score:",score,"-> grade:", get_grade(score))

def count_words(sentence):
    words=sentence.split()
    counts={}
    for word in words:
        if word in counts:
            counts[word]+= 1
        else:
            counts[word]= 1
    return counts
#example
text="the cat sat on the mat the cat ran"
print(count_words(text))

def cart_total(cart):
    total=0
    for item in cart:
        price=cart[item]["price"]
        quantity=cart[item]["quantity"]
        if quantity > 0:
            total+=price*quantity
    return total
#example
cart={
    "apple":{"price":0.5,"quantity":4},
    "bread":{"price":2.5,"quantity":2},
    "milk":{"price":1.2,"quantity":3}
}
print(cart_total(cart))

def is_prime(n):
    if n <= 1:
        return false
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def filter_prime(numbers):
    prime = []
    for num in numbers:
        if is_prime(num):
            prime.append(num)
    return  prime
#example
numbers = [4, 7, 10, 13, 15, 17, 18, 19]
print(filter_prime(numbers))

