
def find_common_participants(group1, group2, r='|'):
    participants1=group1.split(r)
    print(participants1)
    participants2 = group2.split(r)
    spisok = list(set(participants1) & set(participants2))
    spisok.sort()
    return spisok
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group)
print(result)