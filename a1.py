d1 = {"name": "nameless", "age": 35}
d2 = {"ver": 3.6, "platform": "Linux"}
d3 = {"size": "50MB"}

a = [d for d in [d1, d2, d3]]
print(a)
# a = {**d1, **d2, **d3}


# a.update(d1)
# a.update(d2)
# for key, value in d1.items():
#     a[key] = value
# for key, value in d2.items():
#     a[key] = value
# for key, value in d3.items():
#     a[key] = value
# print(a)
