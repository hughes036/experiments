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
    
    # add:
    # (0, 100)
    # remove:
    # (25, 75)
    # leaves:
    # (0, 25)
    # (75, 100)
    # remove:
    # (1, 100)
    def remove(self, start, end):
        ranges_to_update = [r for r in self.ranges if startInRange(start, r) or endInRange(end, r) or (start <= r[0] and end >= r[1])]
        for r in ranges_to_update:
            self.ranges.remove(r)
            # does range being removed include all of r?
            if start <= r[0] and end >= r[1]:
                # remove the range and add nothing
                continue
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
    r.remove(1, 100)
    print(r.ranges) 
    r.remove(0, 100)
    print(r.ranges) 

if __name__ == "__main__":
    main()
