# pisemky = [0, 2, 0, 1, 1, 3]
# 
# # pisemky_bezne = []
# # for znamka in pisemky:
# #     pisemky_bezne.append(znamka + 1)
# 
# pisemky_bezne = [znamka + 1 for znamka in pisemky]
# 
# print(pisemky_bezne)  # [1, 3, 1, 2, 2, 4]

kilometry = [2.4, 2.6, 0, 3.5, 1.8]
kilometry = [round(beh) for beh in kilometry]
print(kilometry)