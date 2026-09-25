# Learning-to-read set — staged, cumulative

Ten books. Each one adds about eight new words and a few letters, and every later book reuses the
earlier words. Nothing on a page uses a word she has not met yet; `check_vocab.py` enforces that.

- **New word per page**: shown big above the sentence (the `Word` column). Names get the big-word slot
  the first time they appear. Sight words (a, is, on, the …) are introduced silently in the sentence and
  listed per book so you can point them out; they never get the big-word slot.
- Pages 10 and 11 reuse only known words. Page 12 is always a nap, so it still ends like the bedtime set.
- **Cast**, all with decodable names, in order of appearance: Pip (beagle pup, from the farm book), Tip (ginger
  kitten), Mim (grey tabby kitten, from the kittens book), Sam (shaggy sheepdog), Bob (bulldog), Chip
  (chihuahua), Spot (dalmatian), Jack (jack russell), Max (pug), Zip (greyhound).
- Letter order follows a standard phonics sequence: `s a t p i n` → `c k e h r m d` → `g o u l f b` →
  `j v w x y z` → `sh ch th ng ck` → consonant blends.

## Shared style sheet (all ten books)

Very simple, bold, clean picture-book illustration for a child learning to read: flat colours, thick soft black
outlines, big rounded shapes, plain cream background with at most one prop, nothing in the picture that is not
in the sentence, no scenery, no gradients, no texture, no photorealism. Limited palette of five muted colours
plus cream. Dark colours only in outlines and small accents. Friendly, calm mood. No text, letters or numbers
anywhere in the image.

- **Palette:** cream, warm grey, ginger orange, soft blue, grass green.
- **Reference:** work/reading/cast.png (one cast sheet shared by all ten books, made by `cast.py`).

---

## 1. Sit, Pip

- **Letters:** s a t p i n
- **Cast:** Pip, Tip
- **Sight words:** a

| # | Word | Text | Image beat |
|---|------|------|-----------|
| 1 | Pip | Pip. | Pip the beagle pup sitting, looking at the reader. |
| 2 | Tip | Tip. | Tip the ginger kitten sitting. |
| 3 | sit | Sit, Pip. | Pip sitting up straight and proud. |
| 4 | sat | Tip sat. | Tip sitting down beside Pip. |
| 5 | pat | Pat, pat, Pip. | Tip patting Pip's head with one paw. |
| 6 | tap | Tap, tap, tap. | Pip tapping the floor with a paw, small motion marks. |
| 7 | nap | Nap, Pip. | Pip lying down with eyes closed. |
| 8 | tin | A tin. | A tin of food on the floor, Pip sniffing it. |
| 9 | sip | Sip, sip, sip. | Tip sipping from a saucer. |
| 10 | | Pip sat. Tip sat. | Pip and Tip sitting side by side. |
| 11 | | Nap, Pip. Nap, Tip. | Both lying down, eyes closing. |
| 12 | | Nap, nap, nap. | Both asleep, curled together. |

## 2. Mim Is a Cat

- **Letters:** c k e h r m d
- **Cast:** Mim
- **Sight words:** is, on, and

| # | Word | Text | Image beat |
|---|------|------|-----------|
| 1 | Mim | Mim. | Mim the grey tabby kitten sitting. |
| 2 | cat | Mim is a cat. | Mim standing proudly. |
| 3 | mat | Mim sat on a mat. | Mim on a small round mat. |
| 4 | hat | A hat. | A red floppy hat on the floor, Tip peeking at it. |
| 5 | red | Tip sat on a red hat. | Tip sitting on the red hat, squashing it. |
| 6 | cap | Pip and a cap. | Pip wearing a cap. |
| 7 | ham | Ham! Pip sat and sat. | Pip staring at a slice of ham on a plate. |
| 8 | hid | Tip hid. | Tip hiding under the red floppy hat, only her ginger tail showing. |
| 9 | rat | A rat! | A grey toy rat on the floor, Mim wide-eyed. |
| 10 | ran | Mim ran and ran. | Mim running after the toy rat. |
| 11 | | Pip sat. Tip sat. Mim sat. | The three in a row. |
| 12 | | Nap, Mim. Nap, nap, nap. | Mim asleep on the mat, Tip and Pip asleep beside her. |

## 3. Sam the Dog

- **Letters:** g o u l f b
- **Cast:** Sam
- **Sight words:** the, in

| # | Word | Text | Image beat |
|---|------|------|-----------|
| 1 | Sam | Sam. | Sam the big shaggy sheepdog. |
| 2 | dog | Sam is a dog. | Sam standing. |
| 3 | big | Sam is big. | Sam towering next to tiny Tip. |
| 4 | log | Sam sat on the log. | Sam sitting on a log. |
| 5 | dig | Dig, Pip, dig. | Pip digging a hole, dirt flying. |
| 6 | mud | Mud on Pip. | Pip covered in mud spots. |
| 7 | tub | Pip is in the tub. | Pip in a round tin tub with suds. |
| 8 | rub | Rub, rub, rub. | Sam rubbing Pip dry with a towel. |
| 9 | bug | A bug on Tip. | A ladybug on Tip's nose, Tip cross-eyed. |
| 10 | fun | Fun, fun, fun! | Pip, Tip and Sam playing in soap bubbles. |
| 11 | | Sam is big. Pip is in the tub. | Sam beside the round grey tin tub with Pip in it. |
| 12 | | Sam, Pip and Tip nap on the mat. | The three asleep on the mat. |

## 4. Bob and the Box

- **Letters:** j v w x y z
- **Cast:** Bob
- **Sight words:** to, of

| # | Word | Text | Image beat |
|---|------|------|-----------|
| 1 | Bob | Bob. | Bob the wrinkly bulldog. |
| 2 | box | A big box. | Bob beside a big cardboard box. |
| 3 | get | Get in the box, Bob. | Bob with his front paws in the box. |
| 4 | fit | Fit, Bob, fit! | Bob squeezing into the box, bottom sticking out. |
| 5 | yes | Yes! Bob is in the box. | Bob sitting in the box, delighted. |
| 6 | wag | Wag, wag, wag. | Bob's tail wagging above the edge of the box. |
| 7 | jam | Jam on Pip. | Pip with red jam on his nose, a jar beside him. |
| 8 | hop | Hop, Tip, hop. | Tip hopping toward the box. |
| 9 | top | Tip is on the top of the box. | Tip perched on the box flap. |
| 10 | | Pip ran to the box. | Pip running to the box, jam still on his nose. |
| 11 | | Bob is in the box. Tip is on the top. Pip sat. | All three at the box. |
| 12 | | Nap, Bob. Nap in the box. | Bob asleep in the box, Tip asleep on top. |

## 5. Chip the Pup

- **Letters:** sh ch th ng ck
- **Cast:** Chip
- **Sight words:** he, see

| # | Word | Text | Image beat |
|---|------|------|-----------|
| 1 | Chip | Chip. | Chip the tiny chihuahua. |
| 2 | pup | Chip is a pup. | Chip beside big Sam for scale. |
| 3 | ship | A ship in the tub. | A toy sailing ship floating in the tub, Chip looking in. |
| 4 | fish | A fish! | A goldfish in a round bowl, Mim watching. |
| 5 | duck | A duck in the tub. | A yellow rubber duck in the tub, Chip beside it. |
| 6 | kick | Kick, Pip, kick. | Pip kicking a ball. |
| 7 | sing | Sing, Tip, sing. | Tip on a fence, mouth open, moon above. |
| 8 | bath | Bath! Chip is in the bath. | Chip in a small bath with bubbles, his huge upright chihuahua ears sticking out. |
| 9 | rug | Chip is on the rug. | Chip on a striped rug wrapped in a towel. |
| 10 | sock | A sock on Chip. | Chip wearing a sock like a jumper. |
| 11 | | See Chip. He is a pup. He is on the rug. | Chip sitting on the rug. |
| 12 | | Nap, Chip. Nap in the sock. | Chip asleep inside a big sock. |

## 6. Spot and the Frog

- **Letters:** blends (sp, fr, mp, nd, dr, st, lk)
- **Cast:** Spot
- **Sight words:** she, has

| # | Word | Text | Image beat |
|---|------|------|-----------|
| 1 | Spot | Spot. | Spot the dalmatian. |
| 2 | spot | Spot has a spot. | Spot looking at one big round spot on her leg. |
| 3 | frog | A frog! | A green frog on a lily pad, Spot surprised. |
| 4 | jump | Jump, frog, jump. | The frog mid-leap. |
| 5 | pond | The frog is in the pond. | A small pond, frog's head above the water, Spot at the edge. |
| 6 | drip | Drip, drip, drip. | Spot soaked and dripping after jumping in. |
| 7 | nest | Tip sat in the nest. | Tip curled in an empty bird's nest on a low branch. |
| 8 | milk | Milk! Tip ran to the milk. | Tip running to a saucer of milk. |
| 9 | lamp | Mim sat on the lamp. | Mim perched on top of a lampshade. |
| 10 | sand | Spot is in the sand. | Spot digging in a sandpit, sand flying. |
| 11 | | Spot has a spot. She is in the pond. Drip, drip. | Spot standing in the pond. |
| 12 | | Nap, Spot. Nap in the sand. | Spot asleep in the sand, the frog asleep on a rock. |

## 7. Jack Can Run

- **Letters:** blends (st, gr, sn, tr)
- **Cast:** Jack
- **Sight words:** none

| # | Word | Text | Image beat |
|---|------|------|-----------|
| 1 | Jack | Jack. | Jack the jack russell terrier. |
| 2 | can | Jack can jump. | Jack leaping high. |
| 3 | run | Run, Jack, run. | Jack running flat out. |
| 4 | fast | Jack is fast. | Jack running very fast past Sam, speed lines behind Jack, both fully visible. |
| 5 | stop | Stop, Jack, stop! | Jack skidding to a halt, a puff of dust. |
| 6 | stick | Jack has a stick. | Jack with a stick in his mouth. |
| 7 | drop | Drop the stick, Jack. | Jack dropping the stick on the ground. |
| 8 | grab | Grab the stick, Pip. | Pip grabbing the stick. |
| 9 | tug | Tug, tug, tug. | Pip and Jack tugging the stick from both ends. |
| 10 | snap | Snap! | The stick broken in two, both dogs surprised. |
| 11 | | Jack has a stick. Pip has a stick. | Each dog holding half a stick. |
| 12 | | Nap, Jack. Nap, Pip. | Both asleep with their halves of the stick. |

## 8. Max Is Not Big

- **Letters:** blends (ft, mp, sn), th
- **Cast:** Max
- **Sight words:** we

| # | Word | Text | Image beat |
|---|------|------|-----------|
| 1 | Max | Max. | Max the pug. |
| 2 | not | Max is not big. | Max next to huge Sam. |
| 3 | bed | Max has a bed. | Max beside a small round dog bed. |
| 4 | soft | The bed is soft. | Max sinking into the bed, blissful. |
| 5 | rest | Rest, Max, rest. | Max lying in the bed. |
| 6 | snug | Max is snug in the bed. | Max tucked in with a blanket. |
| 7 | bump | Bump! Bob is on the bed. | Bob landing on the bed, Max squashed. |
| 8 | then | Then Tip. Then Mim. Then Pip. | Tip, Mim and Pip piling onto the bed. |
| 9 | shift | Shift, Bob, shift. | Bob shuffling over on the bed to make room, Max, Tip, Mim and Pip squeezed beside him. |
| 10 | | We fit! Yes, we fit. | Max, Bob, Tip, Mim and Pip all together on one bed, squashed and happy. |
| 11 | | The bed is soft. Max is snug. | Bob, Tip, Mim and Pip piled on the bed, Max at the bottom smiling. |
| 12 | | Nap, Max. Nap, Bob, Tip, Mim and Pip. | All asleep in a heap on the bed. |

## 9. Zip Is Fast

- **Letters:** blends (nk, gr, fl), th, ng
- **Cast:** Zip
- **Sight words:** go

| # | Word | Text | Image beat |
|---|------|------|-----------|
| 1 | Zip | Zip. | Zip the greyhound. |
| 2 | thin | Zip is thin. | Zip in profile, very slim. |
| 3 | long | Zip is long. | Zip stretched out, long legs and nose. |
| 4 | past | Zip ran past Jack. | Zip streaking past Jack. |
| 5 | win | Zip can win. | Zip crossing a finish ribbon. |
| 6 | grin | Zip has a big grin. | Zip grinning widely. |
| 7 | pant | Pant, pant, pant. | Zip panting, tongue out. |
| 8 | drink | Drink, Zip, drink. | Zip drinking from a bowl. |
| 9 | flop | Flop! Zip is on the rug. | Zip flopped flat on a rug. |
| 10 | | Go, Zip, go! Zip ran fast. | Zip running across grass, Jack far behind. |
| 11 | | Zip can win. Zip has a big grin. | Zip grinning with the ribbon. |
| 12 | | Nap, Zip. Zip is a fast dog. | Zip asleep on the rug, legs twitching. |

## 10. The Big Nap

- **Letters:** review, plus splash
- **Cast:** everyone
- **Sight words:** none

| # | Word | Text | Image beat |
|---|------|------|-----------|
| 1 | sun | The sun. | A big sun over a garden, Pip and Tip small below. |
| 2 | hot | The sun is hot. | Pip panting under the sun. |
| 3 | shed | Pip is in the shed. | Pip lying in the shade of a shed doorway. |
| 4 | fan | Mim and the fan. | Mim in front of a small fan, fur blowing. |
| 5 | swim | Spot can swim. | Spot swimming in the pond. |
| 6 | splash | Splash! | Jack jumping into the pond, big splash. |
| 7 | wet | Jack is wet. Spot is wet. | Both dripping at the pond edge. |
| 8 | dusk | Dusk. The sun is not hot. | Low sun, lavender sky, the garden. |
| 9 | all | All sat. Sam, Bob, Chip, Spot, Jack, Max, Zip and Pip. | Eight dogs in a row on the grass. |
| 10 | still | Still, still, still. | Sam, Bob, Spot and Jack lying still on the grass, Tip and Mim curled among them. |
| 11 | | Tip is on Sam. Mim is on Bob. Pip is on the rug. | The cats asleep on the dogs. |
| 12 | | Nap, all. Nap in the dusk. | Sam, Bob, Chip, Spot, Jack, Max, Zip, Pip, Tip and Mim all asleep together on the grass at dusk. |
