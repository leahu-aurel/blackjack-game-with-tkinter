BACKGROUND = "lightgrey"

COLORS = ["red","black","green","blue","yellow","orange","pink"]
# to make the ace work the right way(ex. if you have the first card an ace, make it change its value to 1 if sum>21)
def calculateValue(value,tp,sum, values):
    while True:
        for q in range(2,11):
            if "{}".format(q) in value:
                print(values)
                return q
            if "jack" in value or "queen" in value or "king" in value:
                print(values)
                return 10
            if "ace" in value:
                print(values)
                return 11
