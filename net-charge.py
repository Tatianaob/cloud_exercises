preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

pKR = {
    'y':10.07,
    'c': 8.18,
    'k':10.53,
    'h':6.00,
    'r':12.48,
    'd':3.65,
    'e':4.25
}

insulinY = float(preproInsulin.count('y'))
print(insulinY)
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

# Exercise 3: Writing the net charge formula
pH = 0
while (pH <= 14):
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
        for x in ['y','c','d','e']}.values())))
print('{0:.2f}'.format(pH), netCharge)
pH += 1



