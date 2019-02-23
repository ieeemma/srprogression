import struct

class Unlock:
    def __init__(self):
        self.reward_id = 0
        self.is_unlocked = False
        self.is_new = False

class StoryChapter:
    def __init__(self):
        self.levels = [0, 0, 0, 0]

class ProgressionStore:
    def __init__(self):
        self.version = 0
        self.xp = 0
        self.played_before = False
        self.played_tutorial = False
        self.unlocks = []
        self.story_difficulty = [0, 0, 0, 0]
        self.story_chapters = [StoryChapter() for i in range(4)]

    def load(self, path):
        with open(path, 'rb') as progression_store:
            progression_store.read(1)
            self.version = struct.unpack('<i', progression_store.read(4))[0]
            self.xp = struct.unpack('<i', progression_store.read(4))[0]
            self.played_before = struct.unpack('<?', progression_store.read(1))[0]
            self.played_tutorial = struct.unpack('<?', progression_store.read(1))[0]
            num_unlocks = struct.unpack('<i', progression_store.read(4))[0]
            self.unlocks = [Unlock() for i in range(num_unlocks)]
            for i in range(num_unlocks):
                self.unlocks[i].reward_id = struct.unpack('<i', progression_store.read(4))[0]
                self.unlocks[i].is_unlocked = struct.unpack('<?', progression_store.read(1))[0]
                self.unlocks[i].is_new = struct.unpack('<?', progression_store.read(1))[0]
            for i in range(4):
                self.story_difficulty[i] = struct.unpack('<i', progression_store.read(4))[0]
                for j in range(4):
                    self.story_chapters[i].levels[j] = struct.unpack('<?', progression_store.read(1))[0]

    def save(self, path):
        data = b""
        data += struct.pack('<?', False) # garbage byte at start of file
        data += struct.pack('<i', self.version)
        data += struct.pack('<i', self.xp)
        data += struct.pack('<?', self.played_before)
        data += struct.pack('<?', self.played_tutorial)
        data += struct.pack('<i', len(self.unlocks))
        for unlock in self.unlocks:
            data += struct.pack('<i', unlock.reward_id)
            data += struct.pack('<?', unlock.is_unlocked)
            data += struct.pack('<?', unlock.is_new)
        for i in range(4):
            data += struct.pack('<i', self.story_difficulty[i])
            data += struct.pack('<????', *self.story_chapters[i].levels)

        with open(path, 'wb') as out:
            out.write(data)


# debug prints

"""
if __name__ == "__main__":
    se = ProgressionStore()
    se.load()
    print(se.version)
    print(se.xp)
    print(se.played_before)
    print(se.played_tutorial)
    print(se.num_unlocks)
    print("---")
    for unlock in se.unlocks:
        print(".")
        print(unlock.reward_id)
        print(unlock.is_unlocked)
        print(unlock.is_new)
    print("---")
    print(se.story_difficulty)
    for chapter in se.story_chapters:
        print(chapter.levels)
"""    
