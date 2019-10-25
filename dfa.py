if __name__ == '__main__':
    file = open("D:\PycharmProjects\DFA\input.txt")
    line = file.readlines()
    move = line[0].split()
    # print(move)
    # print(len(move))
    q = []  # 状态集
    transfer = []  # 转移函数
    index = 1

    while line[index][0] != "=":
        prel =line[index].split()
        if prel[0] == "->":
            start = prel[1]
            # prel = prel[1:-1] # len(prel) == 2
            del prel[0]
        if prel[0] == "*":
            final = prel[1]
            # prel = prel[1:-1]
            del prel[0]
        q.append(prel[0])  # 将当前行的第一个元素加入状态集
        transfer.append({})
        for m in range(len(move)):
            n = m+1
            transfer[len(q)-1][int(move[m])] = prel[n]
            # print("q = ", q)
            # transfer.append({int(move[m]): prel[n]})
            # print(transfer)
            # print("length of prel = ", len(prel))
            # print("prel[%d] = " % (m+1) + prel[m+1]) # list index out of range
            # print("prel[2] = ", prel[2] # list index out of range
            # print("prel = ", prel)
            # print("-"*100)
        index += 1

    # print("=" * 100)
    # print(prel)
    # print(line[index])
    print(transfer)
    index += 1
    # pres = start
    # m = 0
    for n in range(0, len(line[index])-index):
        temp = start
        prel = line[index].split()  # list index out of range
        for m in range(0, len(prel)):
            for i in range(0, len(q)):
                if temp == q[i]:
                    break
            temp = transfer[i][int(prel[int(m)])]
            # print(prel[int(m)])
            # print(prel)
            i = 0

        index = index + 1
        if temp == final:
            print(1)
        else:
            print(0)
        # print("---"*100)


