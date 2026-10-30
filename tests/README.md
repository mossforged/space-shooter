# Void Crew v0.18 traversal regression suite

Run `python3 -m http.server 8765 --bind 127.0.0.1` from the repository root,
then open `http://127.0.0.1:8765/tests/traversal.html` in a browser.
The page advances the actual exported game functions inside an iframe, freezes
its animation-frame clock, and reports failures in the document. No test library
or browser extension is required. Tests use a fresh arena and intact cover.

Validated in the Codex in-app browser: **153 passed, 0 failed**, for both
the served game and the rebuilt self-contained offline HTML.
The initial 102-case ladder audit reproduced 68 endpoint failures and 14 blocked
ladder paths/approaches before any movement edits (20 passed, 82 failed).

Coverage:
- All 34 ladders across Crosscut, tall Carrion Works, and Broken Freighter:
  both endpoints with held vertical input, standing animation, left/right
  walk-offs, full shaft and 24-pixel approach clearance against crates and walls.
- Both duct directions and return trips on Crosscut and tall Carrion at
  60/120/144 Hz, including attempted jumps under the ceiling, slide timer
  expiration inside the duct, and standing after exit.
- Cover jumps, overhead deck collisions, both Crosscut jet gaps in both
  directions, and unchanged run/slide speed at 60/120/144 Hz.
- Ladder jump/jet interruptions, reverse input, release/repress on stacked
  ladders, actual W/S and arrow keyboard events, and bot continuation.
- Firing, damage, and reload during run/slide/climb/jet; a 10-second bot fight.

The tall map retains its dimensions, floors, ladders, walls, encounters and
selection option. Only obstructing cover props moved. Crosscut's ladder next
to the duct moved from x=550 to x=520 to leave a standing landing.

At a ladder endpoint the actor grounds immediately and clears climb velocity
and animation state. Release/repress vertical movement to use another ladder;
reverse input works immediately. Bots acknowledge the landing in navigation.

`python3 scripts/package-release.py` refreshes the existing self-contained
HTML download and release hash after source changes. Assets remain embedded
in the offline ZIP. Test files are not included in the offline game.
