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
        self.num_unlocks = 0
        self.unlocks = []
        self.story_difficulty = [0, 0, 0, 0]
        self.story_chapters = [StoryChapter() for i in range(4)]

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
