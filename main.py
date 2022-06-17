import time

import screenshot as ss
import reading as r
import writing as w

ss.takescreenshot()
text=r.readscreenshot()
print(text)
time.sleep(3.5)
w.acttyping(text) 