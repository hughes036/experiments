def startInRange(start, range) -> bool:
    return start >= range[0] and start <= range[1]

def endInRange(end, range) -> bool:
    return end >= range[0] and end <= range[1]

class Range:

    ranges = []

    def __init__(self):
        self.ranges = []

    def add(self, start, end):
        self.ranges.append((start, end))
    
    def remove(self, start, end):
        # Find ranges that start / end partially overlap with, or are entirely contained by.
        ranges_to_update = [r for r in self.ranges if startInRange(start, r) or endInRange(end, r) or (start <= r[0] and end >= r[1])]
        for r in ranges_to_update:
            self.ranges.remove(r)
            # Does range being removed overlap with r partially?
            if start > r[0] or end < r[1]:
                if start > r[0]:
                    self.add(r[0], start - 1)
                if end < r[1]:
                    self.add(end + 1, r[1])

    def query(self, value) -> bool:
        ranges_including_value = [r for r in self.ranges if value >= r[0] and value <= r[1]]
        return len(ranges_including_value) > 0

def main():
    r = Range()
    r.add(0, 100)
    print(r.ranges)
    r.remove(25, 75)
    print(r.ranges)
    r.remove(80, 200)
    print(r.ranges)
    r.remove(-100, -1) # no-op
    print(r.ranges)  
    r.remove(101, 200) # no-op
    print(r.ranges)
    r.remove(0, 100)
    print(r.ranges) 

if __name__ == "__main__":
    main()
