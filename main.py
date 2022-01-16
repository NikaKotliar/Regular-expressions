from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

result = []
for contact in contacts_list[1:]:
  result1 = re.sub(r"(\+7|8|7)?\s*\((\d+)\)\s*(\d+)\-(\d+)\-(\d+)\s\S+\s(\d+)\S?", r"7(\2)\3-\4-\5 доб.\6 ", contact[5])
  result1 = re.sub(r"[+]*[^\d,]*\d[^\d,]*(\d{3})[^\d,]*(\d{3})[^\d]*(\d{2})[^\d]*(\d{2})", r"+7(\1)\2-\3-\4", result1)
  contact[5]=result1
  FIO = contact[0]+' '+contact[1]+' '+contact[2]+' '
  FIO1 = FIO.split(' ')
  FIO2 = [value for value in FIO1 if value]
  contact[0] = FIO2[0]
  contact[1] = FIO2[1]
  if len(FIO2) > 2:
    contact[2] = FIO2[2]
  result.append(contact)

for i in range(len(result)-1):
  for j in range(i+1, len(result)):
    if result[i][0] == result[j][0] and result[i][1] == result[j][1]:
      for r in range(len(result[i])):
        if result[j][r] > result[i][r]:
          result[i][r] = result[j][r]

doubled = result.copy()
for i in range(len(result)-1):
  for j in range(i+1, len(result)):
    if result[i][0] == result[j][0] or result[i][1] == result[j][1]:
      doubled.remove(result[j])

# TODO 2: сохраните получившиеся данные в другой файл
with open("phonebook.csv",  "w",encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(doubled)