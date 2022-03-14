import re
raw_data = """
ORIGIN      
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//
"""

x = re.sub("\s", " ", raw_data, 2)
print(x)

# Deleting the word, "ORIGIN"
# Deleting the number, "1"
# Deleting the number, "61"
# Deleting 