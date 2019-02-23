# srprogression
Speedrunners Progression Store file editor

This example code generates a 100% save file:
```py
import progression_store

ps = progression_store.ProgressionStore()
ps.version = 5
ps.xp = 999999
ps.played_before = True
ps.played_tutorial = True

ps.unlocks = []
for i in range(1, 353):
  unlock = progression_store.Unlock()
  unlock.reward_id = i
  unlock.is_unlocked = True
  unlock.is_new = False
  
  ps.unlocks.append(unlock)
  
ps.story_difficulty = [4, 4, 4, 4]
ps.story_chapters = []
for i in range(4):
  chapter = progression_store.StoryChapter()
  chapter.levels = [True, True, True, True]
  ps.story_chapters.append(chapter)

ps.save("SpeedRunnerHDProgressionStore")
```
To find or replace `SpeedRunnerHDProgressionStore`, go to `{STEAM}/userdata/{ID}/207140/remote/` where `{STEAM}` is your Steam install directory and `{ID}` is your Steam ID3 associated with your account.
