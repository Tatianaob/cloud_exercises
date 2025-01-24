# ORIGIN      
#         1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
#       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
# //

humanInsulin = "1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed 61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn"

newHumanInsulin = ""

for char in humanInsulin:
        if not char.isdigit() and char != " ":
                newHumanInsulin += char
print(newHumanInsulin)
print(len(newHumanInsulin)) #110 

lsInsulinSeq = newHumanInsulin[0:24:1]
print(lsInsulinSeq)
print(len(lsInsulinSeq))    # 24 chars

binsulinSeq = newHumanInsulin[24:54:1] #30 chars
cinsulinSeq = newHumanInsulin[54:89:1] #35 chars
ainsulinSeq = newHumanInsulin[89::]  #21 chars
