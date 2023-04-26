#Question 1
def lists(list1, list2):
 list3 = []

 for elements in list1:
   if elements in list2:
      list3.append(elements)
 return list3
list1 = [1,2,3,4,5,6,7]
list2 = [4,5,6,7,8,9,10]
list3 = lists(list1, list2)
print(list3)

#Question 2
def palindromes(words):
    palindromes = []
    for word in words:
        if word == word[::-1]:
            palindromes.append(word)
    return palindromes

#Question 3
def primes(numbers):
    is_prime = [True] * (max(numbers) + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(len(is_prime) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, len(is_prime), i):
                is_prime[j] = False
    primes = [num for num in numbers if is_prime[num]]
    return primes

#Question 4
def anagrams(word, word_list):
    word_chars = sorted(word.lower().replace(' ', ''))
    anagrams = []
    for w in word_list:
        if sorted(w.lower().replace(' ', '')) == word_chars:
            anagrams.append(w)
    return anagrams