from queue import Queue

with open("members.txt", "r") as f:
    members = [line.rstrip() for line in f]


friends_05 = {}
with open("friends05.txt","r") as f:
    for line in f:
        pair = (line.strip()).split(" ")
        if pair[0] not in friends_05.keys():
            friends_05[pair[0]] = []
        friends_05[pair[0]].append(pair[1])

friends_10 = {}
with open("friends10.txt","r") as f:
    for line in f:
        pair = (line.strip()).split(" ")
        if pair[0] not in friends_10.keys():
            friends_10[pair[0]] = []
        friends_10[pair[0]].append(pair[1])

seen = []
biggest_05 = []
size_05 = 0

for member in members:
    if member not in seen:
        seen.append(member)
        group = [member]
        q = Queue()
        q.put(member)
        while not q.empty():
            current = q.get()
            if current not in seen and current not in group:
                seen.append(current)
                group.append(current)
            if current in friends_05.keys():
                friends = friends_05[current]
                for i in friends:
                    if i not in seen and i not in group:
                        q.put(i)
        if len(group) > size_05:
            biggest_05 = group
            size_05 = len(group)

seen = []
biggest_10 = []
size_10 = 0

for member in members:
    if member not in seen:
        seen.append(member)
        group = [member]
        q = Queue()
        q.put(member)
        while not q.empty():
            current = q.get()
            if current not in seen and current not in group:
                seen.append(current)
                group.append(current)
            if current in friends_10.keys():
                friends = friends_10[current]
                for i in friends:
                    if i not in seen and i not in group:
                        q.put(i)
        if len(group) > size_10:
            biggest_10 = group
            size_10 = len(group)


print(biggest_05)
print(size_05)
print(" ")
print(biggest_10)
print(size_10)
