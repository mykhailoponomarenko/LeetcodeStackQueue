class FreqStackNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class FreqStack:
    def __init__(self):
        self.freq_map = {}
        self.heads = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq = self.freq_map.get(val, 0) + 1
        self.freq_map[val] = freq
        if freq > self.max_freq:
            self.max_freq = freq
        node = FreqStackNode(val)
        if freq not in self.heads:
            self.heads[freq] = node
        else:
            node.next = self.heads[freq]
            self.heads[freq] = node

    def pop(self) -> int:
        if self.max_freq == 0:
            return None
        val = self.heads[self.max_freq].val
        self.heads[self.max_freq] = self.heads[self.max_freq].next
        self.freq_map[val] -= 1
        if not self.heads[self.max_freq]:
            del self.heads[self.max_freq]
            self.max_freq -= 1
        return val