# n = طول
# m = عرض
# کاشی = مستطیل
# عرض کاشی = ۴
# طول کاشی = ۵
# هدف: چقدر باید کاشی تهیه بشود برای کف استخر دانشگاه؟
n,m = map(int, input().split()) 
n = n *100
m = m *100

x,y = 5, 4


area_tile = x * y
area_uni = n * m 

result = int(area_uni / area_tile)

print(result)

