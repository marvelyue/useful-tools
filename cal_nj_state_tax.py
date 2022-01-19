import argparse

SEPARATED_BRACKETS = [[20000, 0.014], [35000, 0.0175], [40000, 0.035], [75000, 0.05525], [500000, 0.0637]]
JOINT_BRACKETS = [[20000, 0.014], [50000, 0.0175], [70000, 0.0245], [80000, 0.035], [150000, 0.05525], [500000, 0.0637]]


def cal(value, brackets):
    ind = 0
    tax = 0
    while ind < len(brackets):
        if value > brackets[ind][0]:
            tax += (brackets[ind][0] - brackets[ind - 1][0]) * brackets[ind][1] if ind > 0 else brackets[ind][0] * brackets[ind][1]
        else:
            tax += (value - brackets[ind - 1][0]) * brackets[ind][1] if ind > 0 else value * brackets[ind][1]
            break
        ind += 1
    return tax


def cal_tax(args):
    if args.joint == "true":
        return cal(int(args.value), JOINT_BRACKETS)
    return cal(int(args.value), SEPARATED_BRACKETS) * 2


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--value", help="$")
    parser.add_argument("-j", "--joint", help="Whether is joint")
    args = parser.parse_args()
    val = cal_tax(args)
    tax_type = "Joint" if args.joint == "true" else "Separated"
    print("{} total tax: {}".format(tax_type, val))
