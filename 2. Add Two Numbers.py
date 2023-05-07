class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    answer = []
    tens = 0
    for x in range(max(len(l1), len(l2))):

        if len(l1) > 0:
            a = l1.pop()
        else:
            a = 0
        if len(l2) > 0:
            b = l2.pop()
        else:
            a = 0

        res = a + b
        if res >= 9:
            answer.append(tens + res - 10)
            tens = (tens + res) // 10
        else:
            answer.append(tens + res % 10)
            tens = 0
    if tens > 0:
        answer.append(tens)
    return answer


if __name__ == '__main__':
    l3 =[9, 9, 9, 9, 9, 9, 9]
    l4 = [9, 9, 9, 9]
    print(addTwoNumbers(l3, l4))
