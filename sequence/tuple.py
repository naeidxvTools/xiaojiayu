# 元组是不可以改变的  -- 带上枷锁的列表

tuple1 = (1, 2, 3, 4, 5, 7, 8, 9)

print(tuple1[2])
print(tuple1[5:])

# tuple1[2] = 10 # 报错

temp = (10, )

print(temp)

temp = 1,
print(type(temp))

print(8 * (8))

print(8 * (8, ))

