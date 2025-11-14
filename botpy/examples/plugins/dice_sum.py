import os
import random

def DiceSum(dice_str, num_str):
    try:
        dice = int(dice_str.partition('d')[2])
        num = int(num_str)
        print(num)
        print(dice)
        if IsValid(dice) == False:
            resultmsg = f"没见过这种骰子，你给我买一个"
        else:
            sum = 0
            resultmsg = f"骰子面数{dice}，个数{num}\n"
            if num == 1:
                sum = random.randint(1, dice)
                resultmsg += f"你roll出了{sum}!"
            else:
                resultmsg +=f"你roll出了{num}次\n骰子当啷作响\n分别掷出了：\n"
                for i in range(num):
                    value = random.randint(1, dice)
                    resultmsg += f" {value} "
                    sum += value
                resultmsg += f"\n最终值为{sum}"
            resultmsg += f"\n祝你好运~"
    except ValueError:
        print("无法转换为整数")
        resultmsg = "骰子数量输入有问题，用整数尝试下"
    return resultmsg
valid_dices = {4,6,8,10,12,20,100}
def IsValid(dice):
    if dice in valid_dices:
        print('骰子面数存在于列表中')
        return True
    else:
        print('骰子面数不在列表中')
        return False
