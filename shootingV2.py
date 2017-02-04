import random
print ("\n三个牛仔同一时间开枪，每个牛仔随机选择射击另外两个中的一个，")
print ("问：这三个牛仔(1)至少有一个毫发无损(2)全部死亡的概率多少？")

ok=0
die=0

timers=1000
for timer in range (0,timers):
    s1 = random.randint(1,6)
    s2 = random.randint(1,6)
    s3 = random.randint(1,6)
    p1 = 1
    p2 = 1
    p3 = 1

    if s1 <= 3:
       p2=0
    else:
       p3=0

    if s2 <= 3:
       p3=0
    else:
       p1=0

    if s3 <= 3:
       p1=0
    else:
       p2=0

    if p1+p2+p3 >= 1 :
        ok = 1+ ok

    if p1+p2+p3 == 0 :
        die = 1+ die


    # print ("%4d %d %d %d %d %d %d => %d" % (1+timer,s1,s2,s3,p1,p2,p3, p1+p2+p3))

print ("%s %d / %d => %.2f" % ("(1)至少有一个毫发无损",ok, timers, ok/timers))
print ("%s %d / %d => %.2f" % ("(2)全部死亡",die, timers, die/timers))
