
# Huffman Coding in python

string = 'BCAADDDCCACACACCC'


# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    print(node)
    (l, r) = node.children()
    # print(f"l : {l}")
    # print(f"r : {r}")
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


# Calculating frequency
# freq = {'B': 1, 'C': 8, 'A': 5, 'D': 3, 'E':24}
freq = {"0": 23, "51": 8, "102": 4,"153": 24,"204": 4,"255": 1}
# for c in string:
#     if c in freq:
#         freq[c] += 1
#     else:
#         freq[c] = 1
# print(freq)
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print(freq)


nodes = freq


while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    print(nodes)
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    

huffmanCode = huffman_code_tree(nodes[0][0])

print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))