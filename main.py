ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

unic_ID = []
for reo_ID in ids.values():
    unic_ID += reo_ID
    unic_ID = sorted(set(unic_ID))
print(unic_ID)


