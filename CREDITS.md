# Asset credits and provenance

## Kenney sound effects

Files in audio/: blaster, blaster_repeater, enemy_attack, enemy_destroy, enemy_hurt,
jump_a, land, walking and weapon_change (.ogg).

Author: Kenney. Official source: https://github.com/KenneyNL/Starter-Kit-FPS
Pinned commit: 185fd2326d74a5cf858cffc616f87cf9696f9cc0.
The upstream README explicitly states: “Assets included in this package (2D sprites,
3D models and sound effects) are CC0 licensed”. License: CC0 1.0 Universal:
https://creativecommons.org/publicdomain/zero/1.0/

Original audio files are copied unchanged; runtime playback changes volume/pitch
and layers sounds. The upstream README and MIT repository license are preserved
in licenses/. No upstream game code was copied. CC0 sounds may be used commercially;
credit is included voluntarily. No account, attribution overlay or online request
is required by the game.

## Scavenger atlas

art/scavengers.png is new AI-generated artwork created for this project during the
v0.7 pass, using the user's gritty hybrid pixel-art direction. It is not a recovered
original asset or a Kenney asset, and is not represented as third-party CC0 art.
It contains three original scavenger designs in standing and crouched poses;
runtime compositing mixes heads, armor, animation and independent weapons.
The unmodified generated source remains in /workspace/generated_images.

Additional geometry, effects, weapon overlays and ambience are code-authored for
this prototype. No third-party music is used.

art/ship_modules.png is a second new AI-generated atlas of four original modular
wall treatments (cargo, bridge, reactor, maintenance). It is assembled in the
background cache behind separate geometry and props; it is not a flattened level.


## Hullbreak v0.9 original generated assets

- art/orbital_graveyard.png: distant spacecraft wreck and planet vista. Generated
  source: /workspace/generated_images/exec-1209ebe3-8a96-4112-a770-ae1b41163a5c.png.
- art/hull_props.png: cargo crate, control cabinet, crimson banner, coolant pump,
  structural girder and caged work light. Source:
  /workspace/generated_images/exec-1d3ca127-5069-4c22-babc-88ea37362a45.png.
- art/arsenal.png: five futuristic industrial side-profile guns and power-cartridge box. Source:
  /workspace/generated_images/exec-c1fd740e-c526-4f75-b16e-b68a13d457f2.png.

Created for this project with OpenAI image generation using the user-supplied
Void Crew concept as a visual reference. These are new generated assets, not
recovered original production art, third-party downloads or CC0 claims. Generated
PNGs are copied unchanged; runtime code selects frames, scales, composites and
lights them. Original source files are retained. No new external sound assets.


## Dead Reckoning v0.10 character rigs

Original generated transparent nine-part atlases based on the existing scavenger
identities, created with OpenAI image generation for this project:

- art/rig_rust.png — source /workspace/generated_images/exec-cb742e8f-d272-4d00-a8dc-496d1572c5f3.png
- art/rig_cobalt.png — source /workspace/generated_images/exec-34933af7-ff3d-427c-ac3c-9fae3b86bede.png
- art/rig_moss.png — source /workspace/generated_images/exec-5d9f02e0-3716-421d-91b5-ee2d54c550b7.png

Generated PNGs are copied unchanged; the game selects/caches individual parts and
composes them with code-authored skeletal animation. These are not recovered
original production assets or third-party CC0 claims. Source images are retained.
The original full-character atlas remains the loading fallback. No new sound files.


## Blackwater v0.11 environment assets

New original assets generated with OpenAI image generation for this project,
using the user-supplied Void Crew concept as a visual reference:

- art/deep_space.png — far planet/stars only. Source:
  /workspace/generated_images/exec-57c4fba1-2658-4e1d-9540-616f542be853.png
- art/derelict_layer.png — isolated transparent distant freighter. Source:
  /workspace/generated_images/exec-0143dc20-c566-4168-9447-f80b4e2f6ffa.png
- art/blackwater_rooms.png — four recessed room-wall modules. Source:
  /workspace/generated_images/exec-436cb99c-6bf8-4a6a-b1d0-78f8effe224a.png
- art/hull_structure.png — separate deck, rib, cable, torn hull, portal and crane.
  Source: /workspace/generated_images/exec-7d92926d-3e94-4341-9a13-d73b17daa8e1.png

Generated PNGs are copied unchanged; the runtime selects frames, builds caches,
tints nearer wreck pieces and composites independent depth planes. These are not
recovered original production sprites, third-party downloads or CC0 claims. The
original combined vista and wall atlas remain loading fallbacks. No new audio.


## Carrion Tide v0.12 original assets

Created with OpenAI image generation for this project, following the established
weathered Void Crew direction. Generated PNGs are copied unchanged; the runtime
crops frames and composes rooms, weapon grips and enemy attack poses. These are
original generated assets, not recovered production art or third-party CC0 claims.

- art/carrion_rooms.png — dock, foundry, bilge and crew room modules. Source:
  /workspace/generated_images/exec-ec4af67e-566f-4c59-bd03-2a7e35d0b157.png
- art/ship_life.png — drone, mite and turret with attack poses. Source:
  /workspace/generated_images/exec-32deb8d4-66c1-4809-9325-cb069e8d5049.png
- art/salvage_arsenal.png — arc/plasma weapons, nest and three gear items. Source:
  /workspace/generated_images/exec-fd68b55d-34e1-42b6-bfbf-71581c5acbb5.png

Existing licensed sounds are reused with code-synthesized new cues. No additional
third-party audio files or licenses were introduced.


## Pressure Point v0.13

Reuses the existing generated PNGs and licensed audio unchanged. Readability,
enemy poses/death remains, muzzle transitions, discharge effects and match cues
are code-authored. No new third-party assets or licenses were introduced.


## Follow Through v0.14 action components

- art/action_parts.png — original generated transparent four-column, three-row
  sheet: reach hand, brace hand, skid boot and swept cloth in rust, cobalt and moss.
  Created with OpenAI image generation using the existing three original rig
  sheets as references. Source retained unchanged at:
  /workspace/generated_images/exec-b1aa4d69-e4a0-4413-9435-15843eb2f11b.png

The PNG is copied unchanged. Runtime-authored crops, keyframes, pose blending and
limb solving compose these parts with the existing rigs. This is original generated
project art, not a recovered production sprite sheet or third-party CC0 claim.
Existing licensed audio is reused; no additional third-party sounds or licenses.


## Blowback v0.15

No new asset files. Cosmetic ragdoll-style motion and armored fragments reuse the
existing generated modular rigs with mixed cosmetics. Explosion plumes, flame
shapes, pressure rings, sparks and small stylized fragment-end accents are drawn
and cached by code. Existing licensed audio is reused without new licenses.


## Dead Weight v0.16

No new asset files. Pose-aware collision, material responses, contact shadows and
support/sleep logic are code-authored and reuse the existing original sprite rigs
and licensed audio. No additional third-party dependencies or licenses.


## Shipwright v0.17

`art/shipwright_rooms.png` is original generated project art, created with OpenAI
image generation using the user's supplied concept illustration and the project's
existing Carrion room atlas as style references. It contains three panoramic room
backgrounds: salvage foundry, abandoned crew habitat and coolant return. The generated
PNG is copied unchanged; runtime-authored crop regions select the usable strips.
Original generation is preserved in the workspace as
`generated_images/exec-0c06f69d-312a-4574-a475-9fc0b79e2f5c.png`.
This is not a recovered production asset or a third-party CC0 asset. Hull plates,
wear, pipe runs, cable slack, support details, route paint and ambient accents are
code-authored. Existing licensed audio is reused without additional licenses.


## Crosscut v0.18

No new asset files. The compact arena, route graph placement, scenery composition,
lighting locations and encounter/supply placements are code-authored. Existing
original generated artwork and licensed audio are reused unchanged.
