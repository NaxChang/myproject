# data = [(1, 2), (3, 1), (5, 8)]


# sorted_data = sorted(data, key=lambda x: x[1], reverse=False)

# print(sorted_data)
# print(get_second_element(data[0]))

# sorted_data = sorted(data, key=get_second_element)

# def g(x):
#     return x + 1


# print(g(1))


# g = lambda x: x + 1
# print(g(1))

# g1 = lambda x, y: x + 2 * y
# print(g1(1, 2))

# items = [(1, "a"), (3, "b"), (2, "c")]
# items.sort(key=lambda x: x[0])
# print(items)
data1 = ["Nameless", "Python", "Git", "linux", "apple"]

# print(sorted(data1, key=lambda x: x.lower()))
print(sorted(data1, key=str.lower))
