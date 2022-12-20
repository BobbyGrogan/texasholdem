def present():
        #pairs in hand, one pair on board, two pairs on board, three of a kind on board, four of a kind on board
        #full house on board, pair between, three of a kind between, four of a kind between, if two pairs between
        #if full house between
        summary = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        inc = 0
        while inc < 100000:
                bruh = make_deck()
                go = distribute(4, bruh)
                result = comp_pairs(go[1], go[0][0])
                if result[0][0] is not False:
                        summary[0] += 1
                if result[1][0] is not False:
                        if isinstance(result[1][0], list):
                                summary[2] += 1
                        else:
                                summary[1] += 1
                if result[1][1] is not False:
                        summary[3] += 1
                        if result[1][0] is not False:
                                summary[5] += 1
                if result[1][2] is not False:
                        summary[4] += 1 
                if result[2][0] is not False:
                        summary[6] += 1
                        if isinstance(result[2][0], list):
                                summary[9] += 1
                if result[2][1] is not False:
                        summary[7] += 1
                        if result[2][0] is not False:
                                summary[10] += 1
                if result[2][2] is not False:
                        summary[8] += 1
                inc += 1
        return summary

print("pairs in hand, one pair on board, two pairs on board, three of a kind on board, four of a kind on board, full house on board, pair between, three of a kind be>
print(present())

