
print(sum(x**2 for x in [4,5,6] if x % 2 == 0))
    


def word_count(words): return max(words, key=len)


print(word_count(["apple", "banana", "apple", "pie"]))